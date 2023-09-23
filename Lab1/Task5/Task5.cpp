// Task5.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <fstream>
#include <vector>

// Сигнатура архива
const std::string archiveSignature = "ARCHIVE";

// Структура заголовка архива
struct ArchiveHeader {
    std::string signature;
    int version;
    int compressionAlgorithm; // Код алгоритма сжатия (0 - без сжатия)
    int errorCorrectionAlgorithm; // Код алгоритма защиты от помех (0 - без защиты)
    long originalSize; // Размер оригинального файла
};

// Функция кодирования
void Encode(const std::string& inputFile, const std::string& outputFile) {
    // Открываем входной файл для чтения
    std::ifstream input(inputFile, std::ios::binary);
    if (!input) {
        std::cerr << "Ошибка открытия входного файла." << std::endl;
        return;
    }

    // Создаем заголовок архива
    ArchiveHeader header;
    header.signature = archiveSignature;
    header.version = 1;
    header.compressionAlgorithm = 0; // Без сжатия
    header.errorCorrectionAlgorithm = 0; // Без защиты от помех

    // Определяем размер оригинального файла
    input.seekg(0, std::ios::end);
    header.originalSize = input.tellg();
    input.seekg(0, std::ios::beg);

    // Открываем архивный файл для записи
    std::ofstream output(outputFile, std::ios::binary);
    if (!output) {
        std::cerr << "Ошибка открытия архивного файла." << std::endl;
        return;
    }

    // Записываем заголовок в архив
    output.write(reinterpret_cast<const char*>(&header), sizeof(header));

    // Копируем данные из входного файла в архив
    output << input.rdbuf();

    // Закрываем файлы
    input.close();
    output.close();

    std::cout << "Кодирование завершено." << std::endl;
}

// Функция декодирования
void Decode(const std::string& inputFile, const std::string& outputFile) {
    // Открываем архивный файл для чтения
    std::ifstream input(inputFile, std::ios::binary);
    if (!input) {
        std::cerr << "Ошибка открытия архивного файла." << std::endl;
        return;
    }

    // Читаем заголовок архива
    ArchiveHeader header;
    input.read(reinterpret_cast<char*>(&header), sizeof(header));

    // Проверяем сигнатуру архива
    if (header.signature != archiveSignature) {
        std::cerr << "Ошибка: некорректная сигнатура архива." << std::endl;
        return;
    }

    // Проверяем коды алгоритмов сжатия и защиты от помех (если нужно)
    if (header.compressionAlgorithm != 0 || header.errorCorrectionAlgorithm != 0) {
        std::cerr << "Ошибка: неподдерживаемые алгоритмы." << std::endl;
        return;
    }

    // Открываем выходной файл для записи
    std::ofstream output(outputFile, std::ios::binary);
    if (!output) {
        std::cerr << "Ошибка открытия выходного файла." << std::endl;
        return;
    }

    // Копируем данные из архива в выходной файл
    output << input.rdbuf();

    // Закрываем файлы
    input.close();
    output.close();

    std::cout << "Декодирование завершено." << std::endl;
}

int main() {
    // Вызываем функцию кодирования
    Encode("input.txt", "archive.bin");

    // Вызываем функцию декодирования
    Decode("archive.bin", "output.txt");

    return 0;
}
