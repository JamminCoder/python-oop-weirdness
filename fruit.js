class Fruit {
    constructor(data = {color: "unknown"}) {
        this.data = data;
    }

    set_color(color) {
        this.data["color"] = color;
    }

    print_color() {
        console.log("I'm " + this.data["color"])
    }
};


const orange = new Fruit();
orange.set_color("orange");
orange.print_color();


const apple = new Fruit();
apple.print_color();