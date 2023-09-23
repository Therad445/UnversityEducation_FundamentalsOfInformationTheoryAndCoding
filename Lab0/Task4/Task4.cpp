// Task4.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <cstdint>
#include <bitset>

// Функция для упаковки двух беззнаковых чисел v и w (k-битное и (m-k)-битное) в одно m-битное число
uint16_t packNumbers(uint8_t v, uint8_t w, int k, int m) {
    // Проверка на корректность значений k и m
    if (k < 0 || k >= m) {
        std::cerr << "Invalid values of k and m." << std::endl;
        return 0; // Возвращаем ноль в случае ошибки
    }

    // Ограничиваем значения v и w до k и (m-k) бит соответственно
    v &= (1 << k) - 1;
    w &= (1 << (m - k)) - 1;

    // Упаковываем числа с помощью побитовых операций и сдвигов
    uint16_t result = (v << (m - k)) | w;

    return result;
}

// Функция для извлечения двух беззнаковых чисел v и w (k-битное и (m-k)-битное) из 16-битного значения packed
void unpackNumbers(uint16_t packed, uint8_t& v, uint8_t& w, int k, int m) {
    // Проверка на корректность значений k и m
    if (k < 0 || k >= m) {
        std::cerr << "Invalid values of k and m." << std::endl;
        return;
    }

    // Извлекаем числа с помощью побитовых операций и сдвигов
    w = packed & ((1 << (m - k)) - 1);
    v = (packed >> (m - k)) & ((1 << k) - 1);
}

int main() {
    int k = 5;
    int m = 16;

    uint8_t v = 7; // Пример числа v (7 в бинарной форме: 00000111)
    uint8_t w = 3; // Пример числа w (3 в бинарной форме: 00000011)

    uint16_t packedValue = packNumbers(v, w, k, m);
    std::cout << "Packed value: " << packedValue << std::endl;

    uint8_t unpackedV, unpackedW;
    unpackNumbers(packedValue, unpackedV, unpackedW, k, m);
    std::cout << "Unpacked values: v = " << unsigned(unpackedV) << ", w = " << unsigned(unpackedW) << std::endl;

    return 0;
}
