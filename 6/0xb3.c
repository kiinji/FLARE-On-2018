unsigned int checksum_0xb3(char* string, int size) {
    int saved_result = 0;
    unsigned int result = 0xFFFFFFFF; // [sp+2Ch] [bp-Ch]@1
    unsigned int temp_var = 0;
    int i = 0; // [sp+30h] [bp-8h]@2
    int count = 0; // [sp+34h] [bp-4h]@1

    count = 0;
    result = -1;
    while (count < size)
    {
        result ^= string[count];
        for (i = 7; i >= 0; --i) {
            saved_result = result;

            result = result & 1;
            result = ~result + 1;

            temp_var = result;
            result = saved_result;

            result = result >> 1;
            temp_var = temp_var & 0xEDB88320;

            result = result ^ temp_var;
        }
        ++count;
    }

    result = ~result;
    return result;
}