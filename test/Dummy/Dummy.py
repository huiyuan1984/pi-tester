import time


class Dummy_0101:
    '''
    write doc here
    '''
    def __init__(self):
        pass

    def run(self):
        return True, 'call dummy api success'


class Dummy_0102:
    '''
    write doc here
    '''

    def __init__(self):
        pass

    def run(self):
        time.sleep(5)
        return True, 'N/A'


class Dummy_0103:
    '''
    write doc here
    '''

    def __init__(self):
        self.var1 = 'one'   # this variable can be replaced by "-v var1:123"
        self.var2 = 'two'
        pass

    def run(self):
        return False, '<img src="http://www.pccillin.com.tw/sem/images/rightBtn.png">: %s, %s' % (self.var1, self.var2)


class Dummy_0104:
    '''
    write doc here
    '''
    def __init__(self):
        pass

    def run(self):
        return False, 'http://xxx.com.tw'


class Dummy_0105:
    '''
    write doc here
    '''
    def __init__(self):
        pass

    def run(self):
        time.sleep(1)
        return False, ''


class Dummy_0106:
    '''
    write doc here
    '''
    def __init__(self):
        pass

    def run(self):
        return False, ''


class Dummy_0107:
    '''
    write doc here
    '''

    def __init__(self):
        pass

    def run(self):
        return True, ''


class Dummy_0108:
    '''
    write doc here
    '''
    def __init__(self):
        pass

    def run(self):
        return False, ''


class Dummy_0109:
    '''
    write doc here
    '''
    def __init__(self):
        pass

    def run(self):
        return False, ''


class Dummy_0110:
    '''
    write doc here
    '''
    def __init__(self):
        pass

    def run(self):
        return False, ''
