# denite-source-ridgepole

Custom [Denite](https://github.com/Shougo/denite.nvim) source for table definition using [ridgepole](https://github.com/winebarrel/ridgepole).

## Requirements

This is custom source of Denite. You need a properly configured Denite.

## Installation

For vim-plug user,

```
Plug 'xxuxa-k/denite-source-ridgepole'
```

For dein user,

```
call dein#add('xxuxa-k/denite-source-ridgepole')
```

## Settings

Define Schemafile's relative path from your rails project root on your vimrc or init.vim.

```
let g:denite_source_ridgepole#schemafile_path='db/schema/Schemafile'

```

Optionally, define your key map to start `:Denite ridgepole`.

```
nnoremap <Leader>r :Denite ridgepole<CR>
```

## Usage

Just call `:Denite ridgepole`. Keep in mind, however, that this plugin is intended to be used from the rails project root.

## Note

Denite最高
