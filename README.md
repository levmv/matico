# Material Icons Font Customizer :)

A silly script to download Material Icons woff2 font file from google with only specified icons.

Receives name of icons in stdin separated by comma or newline. Generates css
file to STDOUT and downloads woff2 file to current dir.

So, this:
```bash
echo "search, edit, delete" | python3 matico.py
```
will give you:
```css
.icon-delete:before {
 content: '\e872';
}
.icon-edit:before {
 content: '\e3c9';
}
.icon-search:before {
 content: '\e8b6';
}
```

And `icon.woff2` file 744 bytes of size

