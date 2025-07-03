collections = {
    'sideproject1': {
        'driver': 'copy_folder',
        'source': '../../sideproject1/docs/',
    },
    'sideproject2': {
        'driver': 'copy_folder',
        'source': '../../sideproject2/docs/',
    }
}

intersphinx_mapping = {
    'sideproject1': ('https://github.com/GrzegorzSzczepanek/bazy-danych-modele', None),
    'sideproject2': ('https://sideproject2.readthedocs.io/en/latest/', None),
}
