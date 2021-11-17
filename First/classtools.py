# Файл classtools.ру (новый)
"Смешанные утилиты и инструменты для классов"

class AttrDisplay:
    """
    Предоставляет наследуемый метод перегрузки отображения, который показывает
    экземпляры с их именами классов и пары имя=значение для каждого атрибута,
    сохраненного в самом экземпляре (но не атрибутов, унаследованных от его классов) .
    Может соединяться с любым классом и будет работать на любом экземпляре.
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__ ) :
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ','. join(attrs)

    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())

if __name__ == '__main__' :
    class TopTest(AttrDisplay):
        count = 0
        def __init__ (self) :
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            self.attr3 = TopTest.count+2
            TopTest.count += 3
    class SubTest(TopTest) :
        pass
    X, Y, Z = TopTest(), SubTest (), SubTest ()
    print(X)
    print(Y)
    print(Z)
# Создать два экземпляра
# Показать все атрибуты экземпляров
# Показать имя класса, расположенного ниже всех
