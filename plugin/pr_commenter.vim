" --------------------------------
" Add our plugin to the path
" --------------------------------
python3 import sys
python3 import vim
python3 sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
function! PrCommenter()
python3 << endOfPython

from pr_commenter import PrCommenter, VimExt

vim_window = VimExt()

pr = PrCommenter('bisdn', 'basebox')
pr.comments_get()

vim_window.print_lines(pr.comments_output())

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! PrCommenter call PrCommenter()
