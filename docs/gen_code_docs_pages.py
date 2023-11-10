"""Generate the code reference pages and navigation.

Script taken from https://mkdocstrings.github.io/recipes/
"""

from pathlib import Path

import mkdocs_gen_files

# main paths used in this script
package_folder = Path("oktopus")
root_folder = package_folder.parent
code_docs_folder = Path("API Documentation")

# iterate over all python files in the package
for path in sorted(package_folder.rglob("*.py")):

    # imagine path is `src/module.py` (src is defined by `package_folder`` variable)
    doc_path = path.relative_to(package_folder).with_suffix(".md")  # module.md
    module_path = path.relative_to(root_folder).with_suffix("")  # src/module
    full_doc_path = code_docs_folder / doc_path  # as they appear in the mkdocs nav bar

    # if the file is __init__.py, then we want to generate the docs for the folder
    parts = tuple(module_path.parts)
    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
    elif parts[-1] == "__main__":
        continue

    # create markdown file with the documentation of the module.py
    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        module_identification = ".".join(parts)  # pylint: disable=invalid-name
        fd.write(f"::: {module_identification}")  # ::: src.module

    mkdocs_gen_files.set_edit_path(full_doc_path, path)
