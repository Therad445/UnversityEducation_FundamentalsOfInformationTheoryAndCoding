// Task2.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <iomanip>
#include <bitset>
#include <cstdint>

void print32(void* p) {
    // Целочисленные интерпретации
    uint32_t* as_uint32 = reinterpret_cast<uint32_t*>(p);
    int32_t* as_int32 = reinterpret_cast<int32_t*>(p);

    std::cout << "Unsigned Integer (Hex): 0x" << std::hex << *as_uint32 << std::dec << std::endl;
    std::cout << "Unsigned Integer (Binary): " << std::bitset<32>(*as_uint32) << std::endl;
    std::cout << "Unsigned Integer (Decimal): " << *as_uint32 << std::endl;
    std::cout << "Signed Integer (Hex): 0x" << std::hex << *as_int32 << std::dec << std::endl;
    std::cout << "Signed Integer (Binary): " << std::bitset<32>(*as_int32) << std::endl;
    std::cout << "Signed Integer (Decimal): " << *as_int32 << std::endl;

    // Вещественные интерпретации
    float* as_float = reinterpret_cast<float*>(p);

    std::cout << "Float (Fixed): " << std::fixed << std::setprecision(2) << *as_float << std::endl;
    std::cout << "Float (Scientific): " << std::scientific << *as_float << std::endl;
}

int main() {
    // Примеры значений
    uint32_t x = 12345;
    int32_t y = -54321;
    float z = 1234.5678;

    // Вызываем функцию для разных типов значений
    print32(&x);
    print32(&y);
    print32(&z);

    return 0;
}
