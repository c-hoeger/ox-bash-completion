for i in $(<not-done.list); do
    cmdlst=$(/opt/open-xchange/sbin/$i --help 2>/dev/null| grep -Po -- '^[[:space:]](-[a-zA-Z]+)' | sed 's;[[:space:]];;' | tr '\n' ' ')
    cmdlst="$cmdlst
"
    cmdlst="$cmdlst$(/opt/open-xchange/sbin/$i --help 2>/dev/null| grep -- '^ .*--[a-zA-Z].*' | sed 's; .*\(--[-a-zA-Z]*\).*;    \1;' | sort -u)"
    cat<<EOF
_have $i &&
_ox_${i}_completions() {
    local cur prev commandlist

    commandlist='$cmdlst'
    COMPREPLY=()
    _get_comp_words_by_ref cur prev

    COMPREPLY=( \$( compgen -W "\$commandlist" -- "\$cur" ) )
} && complete -F _ox_${i}_completions $i

EOF
done
