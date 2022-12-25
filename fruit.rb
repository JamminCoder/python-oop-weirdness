class Fruit
    def initialize(data = {"color" => "unknown"})
        @data = data
    end

    def set_color(color)
        @data["color"] = color
    end

    def print_color
        puts "I am #{@data["color"]}\n"
    end
end


orange = Fruit.new()
orange.set_color("orange")
orange.print_color

apple = Fruit.new()
apple.print_color()