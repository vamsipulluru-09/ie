#include <stdio.h>
#include <string.h>

// These are special numbers used in our magic math (called CRC)
#define POLYNOMIAL 0xD8
#define TOP_BIT 0x80

// This function creates a "magic number" (called CRC) from a message
unsigned char calculate_crc(unsigned char *message, size_t length) {
    unsigned char result = 0;

    // Go through every letter in the message
    for (size_t i = 0; i < length; ++i) {
        result ^= message[i];  // Mix the letter with the result

        // Do 8 steps of magic math for each letter
        for (unsigned char bit = 8; bit > 0; --bit) {
            if (result & TOP_BIT) {
                result = (result << 1) ^ POLYNOMIAL; // If top bit is 1, mix with polynomial
            } else {
                result = result << 1; // Just shift left
            }
        }
    }

    return result; // This is our final magic number (CRC)
}

int main() {
    unsigned char message[] = "Hello, CRC!"; // This is our message
    unsigned char crc_result = calculate_crc(message, strlen((char *)message)); // Calculate CRC

    printf("Message: %s\n", message); // Show the message
    printf("CRC (Magic Number): 0x%02X\n", crc_result); // Show the CRC in hex format

    return 0;
}