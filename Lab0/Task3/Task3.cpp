// Task3.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <iomanip>
#include <cstdint>
#include <bitset>

void print64(void* p) {
    // Целочисленные интерпретации
    uint64_t* as_uint64 = reinterpret_cast<uint64_t*>(p);
    int64_t* as_int64 = reinterpret_cast<int64_t*>(p);

    std::cout << "Unsigned Integer (Hex): 0x" << std::hex << *as_uint64 << std::dec << std::endl;
    std::cout << "Unsigned Integer (Binary): " << std::bitset<64>(*as_uint64) << std::endl;
    std::cout << "Unsigned Integer (Decimal): " << *as_uint64 << std::endl;
    std::cout << "Signed Integer (Hex): 0x" << std::hex << *as_int64 << std::dec << std::endl;
    std::cout << "Signed Integer (Binary): " << std::bitset<64>(*as_int64) << std::endl;
    std::cout << "Signed Integer (Decimal): " << *as_int64 << std::endl;

    // Вещественные интерпретации
    double* as_double = reinterpret_cast<double*>(p);

    std::cout << "Double (Fixed): " << std::fixed << std::setprecision(2) << *as_double << std::endl;
    std::cout << "Double (Scientific): " << std::scientific << *as_double << std::endl;
}

int main() {
    // Примеры значений
    uint64_t x = 12345678901234567890ULL;
    int64_t y = -1234567890123456789LL;
    double z = 1234.567890123456789;

    // Вызываем функцию для разных типов значений
    print64(&x);
    print64(&y);
    print64(&z);

    return 0;
}
