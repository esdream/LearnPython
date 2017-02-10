class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if not(isinstance(value, int)):
            raise ValueError('width must be a integer')
        if(value < 0 or value > 1024):
            raise ValueError('width must between 0 - 1024')
        else:
            self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if not(isinstance(value, int)):
            raise ValueError('height must be a integer')
        if(value < 0 or value > 768):
            raise ValueError('height must between 0 - 768')
        else:
            self._height = value

    @property
    def resolution(self):
        if not(isinstance(self._height, int) or instance(self._width, int)):
            raise ValueError('width or height error!')
        else:
            self._resolution = self._height * self._width
            return self._resolution

if(__name__ == '__main__'):
    s = Screen()
    s.width = 1024
    s.height = 768
    print(s.resolution)
    assert s.resolution == 786432, '1024 * 768 = %d?' % s.resolution
