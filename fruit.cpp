#include <iostream>
#include <map>

#define FRUIT_MAP std::map<std::string, std::string>

class Fruit {
public:
    FRUIT_MAP data;

    Fruit() {
        this->data["color"] = "unknown";
    };

    Fruit(FRUIT_MAP data) {
        this->data = data;
    }

    void set_color(std::string color) {
        this->data["color"] = color;
    }

    void print_color() {
        std::cout << "I'm " << this->data["color"] << std::endl;
    }
};



int main() {

    Fruit orange = Fruit();
    orange.set_color("orange");
    orange.print_color();

    Fruit apple = Fruit();
    apple.print_color();

    return 0;
}