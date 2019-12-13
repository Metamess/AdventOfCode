
def part1():
    """
    Images are sent as a series of digits that each represent the color of a single pixel.
    The digits fill each row of the image left-to-right, then move downward to the next row,
    filling rows top-to-bottom until every pixel of the image is filled.
    Each image consists of a series of identically-sized layers that are filled in this way.
    The image you received is 25 pixels wide and 6 pixels tall.
    Find the layer that contains the fewest 0 digits. What is the number of 1 digits multiplied by the number of 2 digits?
    """
    image_width = 25
    image_height = 6
    data = read_input()
    layer_size = image_height * image_width
    assert len(data) % layer_size == 0
    layers = [data[i:i+layer_size] for i in range(0, len(data), layer_size)]
    target_layer_id = 0
    min_zeroes = layers[0].count('0')
    for i in range(len(layers)):
        c = layers[i].count('0')
        if c < min_zeroes:
            min_zeroes = c
            target_layer_id = i
    print(layers[target_layer_id].count('1') * layers[target_layer_id].count('2'))


def part2():
    """
    The digits indicate the color of the corresponding pixel: 0 is black, 1 is white, and 2 is transparent.
    The layers are rendered with the first layer in front and the last layer in back.
    What message is produced after decoding your image?
    """
    image_width = 25
    image_height = 6
    data = read_input()
    layer_size = image_height * image_width
    assert len(data) % layer_size == 0
    layers = [data[i:i + layer_size] for i in range(0, len(data), layer_size)]
    image = []
    for j in range(image_height):
        image.append('')
        for i in range(image_width):
            position = j*image_width + i
            for l in layers:
                if l[position] != '2':
                    image[j] += '#' if l[position] == '1' else ' '
                    break
    for row in image:
        print(row)


def read_input():

    with open('input/day8.txt') as input_file:
        return input_file.readline().strip()
