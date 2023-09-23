// Task1.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <iomanip>
#include <bitset>

void print16(void* p) {
    // Преобразуем указатель на void* в указатель на uint16_t*
    uint16_t* ptr = static_cast<uint16_t*>(p);

    // Беззнаковая интерпретация
    unsigned short unsignedValue = *ptr;

    // Шестнадцатеричное представление
    std::cout << "Hex (unsigned): 0x" << std::hex << std::uppercase << unsignedValue << std::dec << std::nouppercase << std::endl;

    // Двоичное представление
    std::cout << "Binary (unsigned): " << std::bitset<16>(unsignedValue) << std::endl;

    // Десятичное представление
    std::cout << "Decimal (unsigned): " << unsignedValue << std::endl;

    // Знаковая интерпретация
    short signedValue = *ptr;

    // Шестнадцатеричное представление
    std::cout << "Hex (signed): 0x" << std::hex << std::uppercase << signedValue << std::dec << std::nouppercase << std::endl;

    // Двоичное представление
    std::cout << "Binary (signed): " << std::bitset<16>(signedValue) << std::endl;

    // Десятичное представление
    std::cout << "Decimal (signed): " << signedValue << std::endl;
}

int main() {
    uint16_t x = 9;
    uint16_t y = static_cast<uint16_t>(-9);
    uint16_t z = 0x88776155;

    std::cout << "Printing 16-bit values:" << std::endl;
    std::cout << "x = " << x << ", y = " << y << ", z = " << z << std::endl;

    std::cout << "Interpretation of x:" << std::endl;
    print16(&x);

    std::cout << "Interpretation of y:" << std::endl;
    print16(&y);

    std::cout << "Interpretation of z:" << std::endl;
    print16(&z);

    return 0;
}
