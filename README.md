Directive For Sphinx
====================================

it is useful if you migrate from sphinx

now you can use these directives

- toctree
- function
- literalinclude

with return nothing (no handle)

for these roles:

- ref
- doc
- download

return raw message

I plan to complete the above corresponding actual functions in the later free time and add more instructions.

doc
------------------

support compute href with old-sphinx-doc-path, 
if your path is ``content/old-doc``, you can set::

    SPHINX_RELATIVE_PATH = "old-doc"

in your config file.

if will find file in "old-doc" when the path can't find in other path.

toctree
------------------

you can use css-class-property "sphinx-toc-tree" to custom your style,
such as::

    .sphinx-toc-tree{
        padding: 2px;
        display: block;
        width: 100px;
        font-size: 19px;
    }






