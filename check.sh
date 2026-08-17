#!/bin/bash
check_quote() {
    file=$1
    phrase=$2
    echo "--- Checking $file for '$phrase'"
    tr '\n' ' ' < "$file" | grep -o -i -E ".{0,40}${phrase}.{0,40}"
}
check_zero() {
    file=$1
    term=$2
    echo "--- Checking ZERO $term in $file"
    tr '\n' ' ' < "$file" | grep -o -i -E ".{0,30}${term}.{0,30}" | head -n 3
}

C="corpus-orig"
check_quote "$C/dk-2025-indfoedsretsproeven.txt" "Den danske stat har eksisteret som selvstændig stat"
check_quote "$C/at-2022-meinoesterreich.txt" "Vor 2000 Jahren lebten Kelten und Römer"
check_quote "$C/ca-2012r2021-discovercanada.txt" "When Europeans explored Canada"
check_quote "$C/ca-2012r2021-discovercanada.txt" "Aboriginals and Europeans formed"
check_quote "$C/de-2025-bamf-gesamtfragenkatalog.txt" "Wann wurde die Bundesrepublik Deutschland gegr"

check_zero "$C/au-2020-our-common-bond-testable.txt" "invasion"
check_zero "$C/de-2025-bamf-gesamtfragenkatalog.txt" "Weimar"
