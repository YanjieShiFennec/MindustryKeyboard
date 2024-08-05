import os


def coordinate_change(from_file, to_file, delta_x, delta_y):
    with open(from_file, "r", encoding="utf-8") as f1, open(to_file, "w", encoding="utf-8") as f2:
        for line in f1:
            if line.startswith("draw rect"):
                datas = line.split(" ")
                datas[2] = str(float(datas[2]) + delta_x)
                datas[3] = str(float(datas[3]) + delta_y)
                new_line = ""
                for i, data in enumerate(datas):
                    new_line += data
                    if (i < len(datas) - 1):
                        new_line += " "
                f2.write(new_line)
            else:
                f2.write(line)


def line_change(from_file, to_file, delta_line):
    with open(from_file, "r", encoding="utf-8") as f1, open(to_file, "w", encoding="utf-8") as f2:
        for line in f1:
            if line.startswith("jump"):
                datas = line.split(" ")
                datas[1] = str(int(datas[1]) + delta_line)
                new_line = ""
                for i, data in enumerate(datas):
                    new_line += data
                    if (i < len(datas) - 1):
                        new_line += " "
                f2.write(new_line)
            else:
                f2.write(line)


def keyboard_input_event_code(to_file, num):
    with open(to_file, "w", encoding="utf-8") as f:
        for i in range(num):
            index = str(i + 1)
            f.write("sensor result" + index + " switch" + index + " @enabled\n")
            f.write("jump " + str((i + 1) * 6) + " equal result" + index + " 0\n")
            f.write("control enabled switch" + index + " 0 0 0 0\n")
            f.write("write " + index + " cell1 0\n")
            f.write("write 1 cell1 1\n")
            f.write("end\n")
        f.write("end\n")


def render_with_offset(from_file, to_file):
    with open(from_file, "r", encoding="utf-8") as f1, open(to_file, "w", encoding="utf-8") as f2:
        for line in f1:
            if line.startswith("draw rect"):
                datas = line.split(" ")
                f2.write("op add x " + datas[2] + " x_offset\n")
                f2.write("op add y " + datas[3] + " y_offset\n")
                f2.write("draw rect x y " + datas[4] + " " + datas[5] + " 0 0\n")
            else:
                f2.write(line)


def jump_line_correction(from_file, to_file, index):
    # index: 判断 key 之前的 jump 数 + 1
    line_count = -1
    jump_line_count = []

    with open(from_file, "r", encoding="utf-8") as f:
        for line in f:
            if not line.startswith("#") and line[0].isalpha():
                line_count += 1
                if line.startswith("jump") and not line.endswith("always\n"):
                    jump_line_count.append(line_count)
    jump_line_count.append(line_count)
    # print(len(jump_line_count))
    for i, e in enumerate(jump_line_count):
        print(e)

    # index = 3
    with open(from_file, "r", encoding="utf-8") as f1, open(to_file, "w", encoding="utf-8") as f2:
        for line in f1:
            if line.find("notEqual key") >= 0:
                datas = line.split(" ")
                f2.write("jump " + str(jump_line_count[index]) + " notEqual key " + datas[4])
                index += 1
            else:
                f2.write(line)


if __name__ == "__main__":
    # line_change("render.txt", "test/test_block_index_render.txt", 6)
    # coordinate_change("mindustry_alphabet_top_left.txt","mindustry_alphabet_top_right.txt", 40, 0)
    # coordinate_change("mindustry_alphabet_top_left.txt","mindustry_alphabet_bottom_left.txt", 0, -40)
    # coordinate_change("mindustry_alphabet_top_left.txt","mindustry_alphabet_bottom_right.txt", 40, -40)
    # keyboard_input_event_code("keyboard_input.txt", 26)
    # render_with_offset("old_render.txt", "new_render.txt")

    # index: 判断 key 之前的 jump 数 + 1
    jump_line_correction("render.txt", "test/test.txt", 2)
    pass
