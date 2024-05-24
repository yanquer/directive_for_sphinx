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

figure
------------------

with STATIC_PATH , auto find where is and convert relative-path to absolute-path


IMAGE_AUTO_ALT
    if auto create alt with "as you see" when alt no set


function
------------------

you should has css like

```css 
/* 新增的 function 指令 */
.rst-function.section{
	margin: 5px 0;
}
.rst-function.section strong{
	background-color: #273f47;
	border-radius: 5px;
	padding: 0 5px;
}
.rst-function.section strong::before{
	font-family: "Font Awesome 6 Free Web";
	content: "\e184";
    margin-right: 0.5em;
}

.rst-function.section > *:not(:first-child){
	margin-left: 1em;
}
```


