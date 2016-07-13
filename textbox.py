
class TextBox():

    def __init__(self, name, color, size):
        self.company_name = name
        self.color = color
        self.size = size



    @staticmethod
    def hex_to_rgb(value):
        if value is None:
            return (0,0,0)
        value = value.lstrip('#')
        lv = len(value)
        if lv == 1:
            v = int(value, 16)*17
            return v, v, v
        if lv == 3:
            return tuple(int(value[i:i+1], 16)*17 for i in range(0, 3))
        return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))

    @staticmethod
    def avg_color(list):
        rgb_sum = (0, 0, 0)
        size = (len(list))
        for i in range(size):
            rgb = TextBox.hex_to_rgb(list[i])
            rgb_sum = (rgb_sum[0] + rgb[0], rgb_sum[1]+rgb[1], rgb_sum[2]+rgb[2])
        avg_rgb = (int(rgb_sum[0]/size), int(rgb_sum[1]/size), int(rgb_sum[2]/size))
        return avg_rgb
