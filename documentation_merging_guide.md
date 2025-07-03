To **link your main repository (repo-wspolne) with other side project repositories** and merge their Sphinx documentation into a single PDF, you have a few effective options depending on your workflow and requirements:

### 1. **Directly Merge Documentation Sources**

- **Checkout or copy the documentation folders** (containing `.rst` files) from each side project into your main documentation project (e.g., as subfolders).
- In your main Sphinx project, **reference these files in your `toctree`** (in `index.rst` or a new master file, like `master.rst`) using relative paths.
- This way, Sphinx treats all the `.rst` files as part of one documentation tree and can generate a single PDF via LaTeX.

**Example structure:**
```
repo-wspolne/
├── docs/
│   ├── index.rst
│   ├── sideproject1/
│   │   └── index.rst
│   └── sideproject2/
│       └── index.rst
```
**Example `toctree` in `index.rst`:**
```rst
.. toctree::
   :maxdepth: 2

   sideproject1/index
   sideproject2/index
```
- All files referenced by `toctree` must be within the Sphinx project directory or its subdirectories, but you can use relative paths like `../sideproject/index.rst` if needed.

### 2. **Use Sphinx-Collections Extension**

- **Sphinx-Collections** is a Sphinx extension that automates collecting `.rst` files from different source folders (even outside your main repo) and integrates them into your documentation build.
- Configure the `collections` variable in your `conf.py` to specify where to pull the documentation from.

**Example `conf.py` snippet:**
```python
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
```
- Reference the collected files in your `toctree` as `_collections/sideproject1/index` etc.

### 3. **Linking (Not Merging) with Intersphinx**

- If you only want to **cross-link** between the documentations (not merge into one PDF), use the **Intersphinx** extension.
- Intersphinx lets you reference sections or objects from other Sphinx projects, and Sphinx will create proper hyperlinks and warn if links break.
- This is best if you want to keep docs separate but easily navigable.

**Example in `conf.py`:**
```python
intersphinx_mapping = {
    'sideproject1': ('https://sideproject1.readthedocs.io/en/latest/', None),
    'sideproject2': ('https://sideproject2.readthedocs.io/en/latest/', None),
}
```
- In your `.rst` files, you can then link like:
  ```
  :ref:`sideproject1:some-section`
  ```

### 4. **Build Multiple PDFs with Shared Chapters**

- If you want to create **multiple PDFs with overlapping content**, Sphinx allows you to specify multiple `latex_documents` in `conf.py`.
- You can also use `include` directives or shared `.rst` files between projects, as long as all referenced files are within the documentation directory.

## **Summary Table**

| Method                | Merges into one PDF | Cross-links only | Keeps repos separate | Automation level |
|-----------------------|:------------------:|:----------------:|:-------------------:|:---------------:|
| Direct merge (copy)   |        Yes         |       No         |         No          |     Manual      |
| Sphinx-Collections    |        Yes         |       No         |        Yes          |    Automated    |
| Intersphinx           |        No          |      Yes         |        Yes          |    Automated    |

**Recommended Approach:**  
If your goal is to produce a **single PDF** with all documentation combined, use either the **direct merge** or **Sphinx-Collections** approach. Sphinx-Collections is especially helpful if you want to automate pulling docs from multiple repositories. If you only need to cross-link between separate documentations, use **Intersphinx**.