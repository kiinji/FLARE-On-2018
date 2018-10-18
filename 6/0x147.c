QWORD checksum_0x147(char cur_char) {
    QWORD v6 = 0;
    QWORD v5 = 1;
    QWORD v4 = 0;

    while (cur_char) {
        v6 = v5 + v4;
        v4 = v5;
        v5 = v6;
        --cur_char;
    }

    return v6;
}