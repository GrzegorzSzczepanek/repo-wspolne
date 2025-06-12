Monitorowanie i diagnostyka 
=====
:Autorzy: - Dominika Półchłopek
	 - Kacper Rasztar
         - Grzegorz Szczepanek

Wstęp
---------

Monitorowanie i diagnostyka baz danych PostgreSQL stanowią fundamentalne elementy zapewniające wydajność, bezpieczeństwo oraz stabilność środowiska produkcyjnego. Nowoczesne rozwiązania monitorowania umożliwiają administratorom proaktywne wykrywanie problemów, optymalizację wydajności oraz zapewnienie zgodności z przepisami bezpieczeństwa. Efektywne monitorowanie PostgreSQL obejmuje szeroki zakres metryk - od aktywności sesji użytkowników, przez analizę operacji na danych, po szczegółowe śledzenie logów systemowych i zasobów na poziomie systemu operacyjnego.

Monitorowanie	Sesji	i	Użytkowników
----------
Analiza	Aktywności	Użytkowników
~~~~~~~~

Systematyczne obserwowanie działań wykonywanych przez użytkowników bazy danych stanowi podstawę skutecznego monitorowania PostgreSQL. Kluczowym narzędziem w tym obszarze jest widok systemowy pg_stat_activity, który umożliwia śledzenie bieżących zapytań, czasu ich trwania oraz identyfikowanie użytkowników i aplikacji korzystających z bazy. Widok pg_stat_activity przedstawia informacje o aktywnych procesach serwera wraz ze szczegółami dotyczącymi powiązanych sesji użytkowników i zapytań. Każdy wiersz w tym widoku reprezentuje proces serwera z danymi o bieżącym stanie połączenia bazy danych.

Praktyczne zastosowanie pg_stat_activity obejmuje monitorowanie aktywności w czasie rzeczywistym oraz generowanie powiadomień w przypadku wykrycia nieprawidłowości. Narzędzia takie jak pgAdmin, Zabbix czy Prometheus wykorzystują te dane do wizualizacji i automatyzacji procesów monitorowania. Administratorzy mogą wykorzystywać proste zapytania SQL do analizy aktywności, na przykład: "SELECT * FROM pg_stat_activity;" pozwala na wyświetlenie wszystkich aktywnych sesji.

Zarządzanie	Zasobami	i	Limity
~~~~~~~~

Efektywne zarządzanie zasobami w PostgreSQL opiera się na odpowiedniej konfiguracji parametrów systemowych takich jak max_connections czy work_mem, które kontrolują liczbę jednoczesnych połączeń i wykorzystanie pamięci. Monitorowanie wykorzystania zasobów realizowane jest poprzez narzędzia systemowe jak top, htop, vmstat czy iostat w środowisku Linux, a także dedykowane rozwiązania do monitorowania baz danych.

Kluczowe metryki obejmują współczynnik trafień cache'u, który powinien utrzymywać się powyżej 99% dla systemów produkcyjnych. Zapytanie sprawdzające ten wskaźnik: "SELECT sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) as ratio FROM pg_statio_user_tables;" pozwala na ocenę efektywności wykorzystania pamięci.

Wykrywanie	Problemów	z	Blokadami
~~~~~~~~

Identyfikacja i analiza blokad stanowi istotny element zapewniający płynność działania aplikacji. PostgreSQL udostępnia widok pg_locks umożliwiający śledzenie blokad i konfliktów między transakcjami. Specjalistyczne narzędzia jak pganalyze oferują zaawansowane funkcje monitorowania blokad z automatycznym wykrywaniem sytuacji deadlock oraz powiadomieniami o potencjalnych zagrożeniach .

Podstawowe zapytanie do identyfikacji nieprzyznanych blokad: "SELECT relation::regclass, * FROM pg_locks WHERE NOT granted;" pozwala na szybkie wykrycie problemów. Bardziej zaawansowane analizy wymagają łączenia informacji z widoków pg_locks i pg_stat_activity w celu identyfikacji procesów blokujących i blokowanych.

Monitorowanie	Dostępu	do	Tabel	i	Operacji	na	Danych
-----------

Analiza	Użycia	Danych
~~~~~~~~

Administratorzy baz danych wykorzystują narzędzia monitorujące takie jak pg_stat_user_tables w PostgreSQL do zrozumienia wzorców wykorzystania tabel oraz identyfikacji najczęściej wykonywanych operacji. Analiza tych danych pozwala zidentyfikować najbardziej obciążone tabele, ocenić rozkład ruchu oraz przewidzieć przyszłe potrzeby związane z rozbudową infrastruktury.

Narzędzia do wizualizacji jak Grafana czy Prometheus umożliwiają prezentację trendów w użyciu tabel i pomagają w planowaniu optymalizacji. Kompleksowe monitorowanie obejmuje śledzenie operacji SELECT, INSERT, UPDATE, DELETE oraz analizę wzorców dostępu do danych w różnych okresach czasowych.

Wykrywanie Nieprawidłowych Zapytań
~~~~~~~~

Do wykrywania zapytań o długim czasie wykonania lub wysokim zużyciu zasobów wykorzystuje się rozszerzenie pg_stat_statements, które pozwala monitorować wydajność zapytań, analizować plany wykonania i identyfikować operacje wymagające optymalizacji. Moduł pg_stat_statements zapewnia śledzenie statystyk planowania i wykonania wszystkich instrukcji SQL wykonywanych przez serwer.

Konfiguracja pg_stat_statements wymaga dodania modułu do shared_preload_libraries w postgresql.conf oraz restartu serwera. Widok pg_stat_statements zawiera po jednym wierszu dla każdej unikalnej kombinacji identyfikatora bazy danych, użytkownika i zapytania, do maksymalnej liczby różnych instrukcji, które moduł może śledzić.

Bezpieczeństwo i Zgodność
~~~~~~~~

Śledzenie dostępu do tabel jest kluczowe z punktu widzenia bezpieczeństwa oraz zgodności z przepisami takimi jak RODO czy PCI DSS. W PostgreSQL do audytu operacji na danych służy rozszerzenie pgaudit, które pozwala rejestrować szczegółowe informacje o działaniach na poziomie zapytań i transakcji. PGAudit zapewnia narzędzia potrzebne do tworzenia logów audytowych wymaganych do przejścia określonych audytów rządowych, finansowych lub certyfikacji ISO.

Systemy takie jak ELK Stack czy Splunk umożliwiają centralizację i analizę logów oraz konfigurację alertów na podejrzane działania, co wzmacnia bezpieczeństwo środowiska bazodanowego. Automatyczne powiadomienia można skonfigurować dla zdarzeń takich jak próby logowania poza godzinami pracy lub masowe operacje na wrażliwych tabelach.

Monitorowanie Logów i Raportowanie Błędów
-----------

Analiza Logów Systemowych
~~~~~~~~

PostgreSQL generuje szczegółowe logi systemowe i dzienniki błędów stanowiące podstawowe źródło informacji o stanie bazy danych. Dzienniki rejestrują wszelkie błędy, ostrzeżenia, nietypowe zdarzenia oraz informacje o operacjach wykonywanych przez użytkowników i aplikacje, obejmując kody błędów, czas wystąpienia problemu, tekst zapytania SQL oraz szczegóły środowiska wykonania.

Regularna analiza logów pozwala administratorom na szybkie wykrywanie i rozwiązywanie problemów przed ich wpływem na użytkowników końcowych. Do analizy wykorzystuje się narzędzia takie jak ELK Stack (Elasticsearch, Logstash, Kibana), Splunk, pgBadger czy wbudowane funkcje PostgreSQL. pgBadger stanowi szczególnie efektywne narzędzie - jest to szybki analizator logów PostgreSQL napisany w Perl, który przetwarza dane wyjściowe logów na raporty HTML z szczegółowymi informacjami o wydajności.

Automatyczne Raportowanie i Alerty
~~~~~~~~

Automatyzacja raportowania i alertowania stanowi kluczowy element szybkiego reagowania na incydenty. Narzędzia takie jak pgAdmin, Zabbix, Prometheus czy Grafana umożliwiają konfigurację reguł automatycznego generowania raportów oraz wysyłania powiadomień przy wykryciu określonych zdarzeń.

Skuteczne alertowanie wymaga ostrożnego ustawiania progów i właściwej priorytetyzacji. Alerty o wysokim priorytecie obejmują opóźnienia replikacji przekraczające 2 minuty, liczę połączeń przekraczającą 85% max_connections oraz współczynnik trafień cache'u spadający poniżej 98% dla systemów produkcyjnych. Powiadomienia mogą być wysyłane poprzez e-mail, SMS, Slack lub inne kanały komunikacji.

Konfiguracja Logowania dla pgBadger
~~~~~~~~

Aby efektywnie wykorzystać pgBadger, logowanie w PostgreSQL powinno być skonfigurowane w sposób zapewniający maksimum informacji. Podstawowe ustawienia konfiguracyjne w postgresql.conf obejmują: log_checkpoints = on, log_connections = on, log_disconnections = on, log_lock_waits = on, log_temp_files = 0, log_autovacuum_min_duration = 0.

Szczególnie wartościowe są raporty wolnych zapytań generowane przez pgBadger, które polegają na ustawieniu log_min_duration_statement. pgBadger może przetwarzać logi PostgreSQL niezależnie od tego, czy są to syslog, stderr czy csvlog, o ile linie logów zawierają wystarczające informacje w prefiksie .

Monitorowanie na Poziomie Systemu Operacyjnego
--------

Narzędzia Systemowe
~~~~~~~~

Monitorowanie zasobów systemowych takich jak procesor, pamięć, dysk i sieć jest kluczowe dla zapewnienia stabilnej pracy PostgreSQL. W środowisku Linux administratorzy wykorzystują narzędzia takie jak top (wyświetlające listę procesów i zużycie zasobów w czasie rzeczywistym), htop (oferujące graficzne przedstawienie obciążenia), iostat (monitorujące statystyki wejścia/wyjścia) oraz vmstat (dostarczające informacji o pamięci i aktywności procesora).

W środowisku Windows popularne narzędzia obejmują Menedżer zadań umożliwiający monitorowanie użycia CPU, pamięci, dysku i sieci przez poszczególne procesy oraz Monitor systemu (Performance Monitor) - zaawansowane narzędzie do śledzenia wielu wskaźników wydajności. Te narzędzia umożliwiają szybkie wykrywanie i diagnozowanie problemów z wydajnością zarówno na poziomie systemu operacyjnego, jak i samej bazy danych.

Efektywne monitorowanie systemu wymaga śledzenia kluczowych metryk: wykorzystania CPU (wysokie użycie może ograniczać przetwarzanie zapytań), CPU steal time (szczególnie w środowiskach zwirtualizowanych), wykorzystania pamięci przez PostgreSQL oraz ogólnego obciążenia pamięci systemu. Krytyczne jest unikanie wykorzystania swap przez PostgreSQL, ponieważ drastycznie pogarsza to wydajność.

Integracja z Narzędziami Zewnętrznymi
~~~~~~~~

PostgreSQL doskonale integruje się z zaawansowanymi narzędziami monitorowania infrastruktury IT, umożliwiającymi centralizację nadzoru oraz automatyzację reakcji na incydenty. Nagios, popularny system monitorowania infrastruktury, pozwala na monitorowanie stanu serwerów, usług, zasobów sprzętowych oraz sieci z konfiguracją alertów powiadamiających o przekroczeniu progów wydajności.

Prometheus stanowi narzędzie do zbierania i przechowywania metryk współpracujące z wieloma eksporterami, w tym dedykowanymi dla PostgreSQL. OpenTelemetry Collector oferuje nowoczesne podejście, działając jako agent pobierający dane telemetryczne z systemów i eksportujący je do backendu OpenTelemetry. Grafana zapewnia zaawansowaną wizualizację danych, umożliwiając tworzenie interaktywnych dashboardów prezentujących kluczowe wskaźniki wydajności PostgreSQL.

Narzędzia Monitorowania PostgreSQL
------

Narzędzia Open Source
~~~~~~~~

Ekosystem narzędzi open source dla PostgreSQL jest bogaty i różnorodny. pgAdmin oferuje graficzny interfejs do administrowania bazami danych z funkcjami monitorowania aktywności serwera, wydajności zapytań oraz obiektów bazy danych. Dashboard serwera w pgAdmin dostarcza przegląd ważnych metryk, w tym wykorzystania CPU, pamięci, miejsca na dysku i aktywnych połączeń.

pgBadger stanowi jedną z najpopularniejszych opcji - to szybki analizator logów PostgreSQL zbudowany dla wydajności, który tworzy szczegółowe raporty w formacie HTML5 z dynamicznymi wykresami. Najnowsza wersja pgBadger 13.0 wprowadza nowe funkcje, w tym konfigurowalne histogramy czasów zapytań i sesji. Narzędzie jest idealne do zrozumienia zachowania serwerów PostgreSQL i identyfikacji zapytań wymagających optymalizacji.

PGWatch reprezentuje kolejne zaawansowane rozwiązanie - to elastyczne, samodzielne narzędzie do monitorowania metryk PostgreSQL oferujące instalację w jedną minutę przy użyciu Dockera. PGWatch charakteryzuje się nieinwazyjną konfiguracją, intuicyjną prezentacją metryk przy użyciu Grafany oraz łatwą rozszerzalnością poprzez definiowanie metryk w czystym SQL.

Rozwiązania Komercyjne
~~~~~~~~

DataDog APM zapewnia komercyjną platformę monitorowania i analizy ze specjalistyczną integracją PostgreSQL. Platforma oferuje łatwą w użyciu integrację PostgreSQL umożliwiającą zbieranie i monitorowanie metryk wydajności bez ręcznej instrumentacji. Agent DataDog automatycznie pobiera metryki PostgreSQL udostępniane przez serwer, obejmując połączenia z bazą danych, wydajność zapytań, statystyki puli buforów oraz status replikacji.

Sematext Monitoring skupia się na logach, infrastrukturze, śledzeniu i monitorowaniu wydajności nie tylko dla PostgreSQL, ale także dla wielu innych baz danych. Rozwiązanie oferuje łatwy w konfiguracji agent PostgreSQL oraz wbudowaną integrację logów PostgreSQL pozwalającą identyfikować wolne zapytania, błędy i ostrzeżenia.

pganalyze stanowi wyspecjalizowane narzędzie monitorowania PostgreSQL umożliwiające optymalizację i analizę zapytań, łatwe monitorowanie bieżących zapytań w czasie rzeczywistym oraz zbieranie planów zapytań. Dzięki kompleksowym danym o wydajności zapytań pganalyze pozwala szybko identyfikować przyczyny problemów i sprawdzać skuteczność wdrożonych rozwiązań.

Zabbix dla PostgreSQL
~~~~~~~~

Zabbix stanowi open-source'owe rozwiązanie monitorowania obsługujące PostgreSQL poprzez wbudowane szablony i niestandardowe skrypty. System opiera się na agentach instalowanych na systemach docelowych - w przypadku PostgreSQL wymaga konfiguracji agenta Zabbix na serwerze PostgreSQL.

Implementacja Zabbix dla PostgreSQL wymaga stworzenia użytkownika monitorowania z odpowiednimi prawami dostępu. Dla PostgreSQL w wersji 10 i wyższej: "CREATE USER zbx_monitor WITH PASSWORD '<PASSWORD>' INHERIT; GRANT pg_monitor TO zbx_monitor;". Po zaimportowaniu szablonu PostgreSQL Zabbix automatycznie zbiera metryki takie jak liczba połączeń, wskaźniki transakcji, wydajność zapytań i inne.

Najlepsze Praktyki Monitorowania
------

Ustanawianie Baselines Wydajności
~~~~~~~~

Tworzenie baselines wydajności stanowi fundament skutecznego wykrywania anomalii. Bez zrozumienia normalnych wzorców zachowania identyfikacja problematycznych odchyleń staje się zgadywaniem zamiast analizy opartej na danych. Kompleksowe ustalanie baselines wymaga zbierania metryk w różnych ramach czasowych i wzorcach obciążenia, obejmując dzienne wzorce (szczczyty w godzinach biznesowych i nocne przetwarzanie), tygodniowe różnice oraz miesięczne i sezonowe wariacje.

Dla każdego wzorca należy dokumentować wskaźniki przepustowości zapytań, poziomy wykorzystania zasobów, zakresy liczby połączeń, wskaźniki transakcji oraz rozkłady zdarzeń oczekiwania. Zaleca się zbieranie co najmniej trzech cykli każdego typu wzorca przed ustaleniem wartości progowych.

Korelacja Metryk Międzysystemowych
~~~~~~~~

Problemy wydajności PostgreSQL rzadko występują w izolacji. Najbardziej wartościowe implementacje monitorowania korelują metryki z różnych podsystemów w celu ujawnienia związków przyczynowo-skutkowych. Efektywne strategie korelacji obejmują łączenie metryk wykonania zapytań z metrykami zasobów systemowych, korelację zdarzeń wdrożeniowych aplikacji z metrykami wydajności bazy danych oraz analizę metryk przy użyciu spójnych okien czasowych.

Implementacja zwykle wymaga ujednoliconego oznaczania czasowego w systemach monitorowania, spójnego tagowania metadanych dla usług i komponentów oraz scentralizowanego logowania zdarzeń systemowych. Narzędzia wizualizacji powinny obsługiwać nakładanie różnych typów metryk w celu efektywnej analizy.

Konfiguracja Efektywnych Alertów
~~~~~~~~

Strategie alertowania wymagają starannego ustawiania progów i właściwej priorytetyzacji. Alerty o wysokim priorytecie wymagające natychmiastowej akcji obejmują opóźnienia replikacji przekraczające 2 minuty, liczę połączeń przekraczającą 85% max_connections, wskaźniki wycofywania transakcji powyżej 10% utrzymujące się przez 5+ minut oraz przestrzeń dyskową poniżej 15% na wolumenach bazy danych.

Alerty o średnim priorytecie wymagające badania obejmują czasy zapytań przekraczające 200% historycznych baselines, nietypowy wzrost użycia plików tymczasowych, rozdęcie tabel przekraczające 30% rozmiaru tabeli oraz brak działania autovacuum przez 24+ godziny. Implementacja wielopoziomowego alertowania z progami ostrzeżeń na poziomie 70-80% wartości krytycznych zapewnia wczesne powiadomienie o rozwijających się problemach.

Monitorowanie Wysokiej Dostępności
------

Monitorowanie Statusu Replikacji
~~~~~~~~

Monitorowanie klastrów PostgreSQL o wysokiej dostępności wymaga dodatkowych wymiarów poza monitorowaniem pojedynczej instancji. Kluczowe obszary obejmują śledzenie opóźnienia replikacji w jednostkach bajtów i czasu, monitorowanie wskaźnika generowania WAL na głównej instancji w porównaniu do wskaźnika odtwarzania na replikach oraz sprawdzanie akumulacji slotów replikacji, które mogą powodować zapełnienie dysku.

Zapytanie monitorujące opóźnienie replikacji: "SELECT application_name, pg_wal_lsn_diff(pg_current_wal_lsn(), replay_lsn) AS lag_bytes FROM pg_stat_replication;" pozwala na wykrywanie rosnącego opóźnienia wskazującego, że repliki nie nadążają za instancją główną. Regularne testowanie możliwości promocji repliki oraz monitorowanie mechanizmów automatycznego failover jest kluczowe dla gotowości na awarię.

Weryfikacja Spójności
~~~~~~~~

Implementacja niezależnego monitorowania każdego węzła klastra z osobną instancją monitorowania poza klastrem bazy danych zapewnia widoczność podczas problemów z całym klastrem. Okresowe sprawdzenie spójności danych między instancją główną a replikami, monitorowanie konfliktów replikacji w konfiguracjach replikacji logicznej oraz śledzenie sum kontrolnych tabel są kluczowe dla utrzymania integralności danych.

Monitorowanie rozkładu połączeń obejmuje śledzenie liczby połączeń na głównej instancji i replikach odczytu, monitorowanie konfiguracji load balancera oraz weryfikację możliwości failover w connection stringach aplikacji. Sprawdzanie nieodpowiednich zapisów kierowanych do replik pomaga uniknąć błędów aplikacyjnych podczas przełączeń.


Wniosek
-----

Monitorowanie i diagnostyka PostgreSQL stanowią kompleksowy proces wymagający holistycznego podejścia obejmującego multiple warstwy systemu. Skuteczna implementacja łączy monitorowanie na poziomie bazy danych, systemu operacyjnego oraz aplikacji, wykorzystując zarówno narzędzia wbudowane w PostgreSQL, jak i zewnętrzne rozwiązania specjalistyczne. Kluczem do sukcesu jest ustanowienie solidnych baseline'ów wydajności, implementacja inteligentnego systemu alertów oraz regularna analiza trendów umożliwiająca proaktywne zarządzanie zasobami i optymalizację wydajności przed wystąpieniem problemów krytycznych.


Bibliografia:
-------

1. https://betterstack.com/community/comparisons/postgresql-monitoring-tools/

2.  https://uptrace.dev/tools/postgresql-monitoring-tools

3. https://documentation.red-gate.com/pgnow

4. https://last9.io/blog/monitoring-postgres/

5. https://stackoverflow.com/questions/17654033/how-to-use-pg-stat-activity

6. https://pganalyze.com/blog/postgres-lock-monitoring

7. https://www.pgaudit.org

8. https://www.postgresql.org/docs/current/pgstatstatements.html

9. https://github.com/darold/pgbadger

10. https://hevodata.com/learn/elasticsearch-to-postgresql/

11. https://www.zabbix.com/integrations/postgresql

12. https://sematext.com/blog/postgresql-monitoring/

13. https://www.alibabacloud.com/help/en/analyticdb/analyticdb-for-postgresql/use-cases/use-pg-stat-activity-to-analyze-and-diagnose-active-sql-queries

14. https://wiki.postgresql.org/wiki/Lock_Monitoring

15. https://severalnines.com/blog/postgresql-log-analysis-pgbadger/

16. https://pgwatch.com

17. https://www.depesz.com/2022/07/05/understanding-pg_stat_activity/

18. https://www.postgresql.org/about/news/pgbadger-v124-released-2772/

19. https://docs.yugabyte.com/preview/explore/observability/pg-stat-activity/

20. https://www.postgresql.org/about/news/pgbadger-130-released-2975/

21. https://techdocs.broadcom.com/us/en/vmware-tanzu/data-solutions/tanzu-greenplum/6/greenplum-database/ref_guide-system_catalogs-pg_stat_activity.html

22. https://www.postgresql.org/docs/current/monitoring.html

23. https://www.reddit.com/r/PostgreSQL/comments/1auy79s/suggestions_for_postgresql_monitoring_tool/

24. https://wiki.postgresql.org/wiki/Monitoring

25. https://www.site24x7.com/learn/postgres-monitoring-guide.html

26. https://www.softwareandbooz.com/introducing-pgnow/

27. https://www.postgresql.org/docs/current/monitoring-stats.html

28. https://docs.dhis2.org/fr/topics/tutorials/analysing-postgresql-logs-using-pgbadger.html

29. https://dev.to/full_stack_adi/pgbadger-postgresql-log-analysis-made-easy-54ki

30. https://support.nagios.com/kb/article/xi-5-10-0-and-newer-postgress-to-mysql-conversion-560.html

31. https://github.com/melli0505/Docker-ELK-PostgreSQL
