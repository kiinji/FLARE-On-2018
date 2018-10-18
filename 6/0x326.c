int main(int argc, char *argv[])
{
    char local_buff[64] = { 0x2A, 0x39, 0x5F, 0x64, 0xC2, 0xA7, 0x46, 0x23, 0x53, 0x6B, 0x74, 0x47, 0x28, 0x4D, 0x70, 0x42, 0x49, 0x25, 0x52, 0x6A, 0x62, 0x38, 0x40, 0x4A, 0x69, 0x45, 0x44, 0x59, 0x2D, 0x31, 0x24, 0x50, 0x67, 0x79, 0x54, 0x21, 0x4C, 0x76, 0x71, 0x66, 0x2B, 0x63, 0x68, 0x6D, 0x51, 0x57, 0x4F, 0x30, 0x65, 0x4E, 0x5A, 0x34, 0x75, 0x6E, 0x33, 0x6C, 0x37, 0x48, 0x26, 0x32, 0x77, 0x61, 0x7A, 0x4B };
    
    std::string key_map = "";
    std::stringstream sstream;

    for (int i = 0x20; i <= 0x7E; i++) {
 // for (int ii = 0x20; ii <= 0x7E; ii++) { 
 // for (int iii = 0x20; iii <= 0x7E; iii++) {

        char temp = 0;
        WORD highLow = 0;
        int crypt_pos = 0;
        char crypt_[5] = { 0, 0, 0, 0, 0 };

        int key_len = 1;
        char key[2] = { 0, 0 };
        key[0] = i;
        //key[1] = ii;
        //key[2] = iii;
        //key[3] = 0;

        bool found = true;

        for (int key_pos = 0; key_pos <= key_len; key_pos++) {
            highLow = (highLow & 0xFF00) + key[key_pos];

            if (key_pos % 3 || key_pos >= key_len) {
                if (key_pos % 3 == 1) {
                    temp = (unsigned char)(highLow >> 4);
                    highLow = (highLow & 0x00FF) + ((highLow & 0xF) << 8);

                    crypt_[crypt_pos++] = local_buff[temp];
                }
                else if (key_pos % 3 == 2) {
                    temp = (unsigned char)(highLow >> 6);
                    if (key[key_pos]) {

                        crypt_[crypt_pos++] = local_buff[temp];
                    }

                    if (key_pos < key_len) {
                        temp = highLow & 0x3F;
                        crypt_[crypt_pos++] = local_buff[temp];
                    }
                }
            }
            else {
                temp = (unsigned char)(highLow >> 2);
                highLow = (highLow & 0x00FF) + ((highLow & 3) << 8);

                crypt_[crypt_pos++] = local_buff[temp];
            }
        }

        sstream << "0x";
        for (int i = 0; i <= key_len; i++) {
            sstream << std::hex << (((unsigned short)crypt_[i]) & 0xff);
        }
        sstream << std::hex << "00";
        sstream << ":" << std::string(key) << "\n";
    }

    key_map = sstream.str();
    std::ofstream out("D:\\CTF\\flare-on-2018\\6\\keymap_326_1.txt");
    out << key_map;
    out.close();
}