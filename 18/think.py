if __name__ == "__main__":
    # 自定义类定义，注意是定义，等于重载 type __call__ 
    class MyMeta(type):
        def __init__(self, name, bases, dic):
            super().__init__(name, bases, dic)
            print("===>MyMeta.__init__")
            print(self.__name__)
            print(dic)
            print(self.yaml_tag)
            
        def __new__(cls, *args, **kwargs):
            print("===>MyMeta.__new__")
            print(cls.__name__)
            return type.__new__(cls, *args, **kwargs)
            
        def __call__(cls, *args, **kwargs):
            print("===>MyMeta.__call__")
            obj = cls.__new__(cls)
            cls.__init__(cls, *args, **kwargs)
            # super().__call__(*args, **kwargs)
            return obj

    # 定义一个类，其实就是 class xxx() = type('xxx', (), {'yaml_tag': '!Foo', ...}) 这等于是 type 执行 __call__, 此方法中有 type.__new__, type.__init__
    # class Foo(metaclass=MyMeta) --> Foo = MyMeta('Foo', (), {'yaml_tag': '!Foo', ...})
    # --> MyMeta.__new__();MyMeta.__init__()
    # 定义 Foo 指定 metaclass 时，等于要生成一个 meta 实例 执行 type.__call__, 而其中就会有 mymeta.__new__, mymeta.__init__
    class Foo(metaclass=MyMeta):
        yaml_tag = "!Foo"
        def __init__(self, name):
            print("Foo.__init__")
            self.name = name
                
        def __new__(cls, *args, **kwargs):
            print("Foo.__new__")
            return object.__new__(cls)
    # 当 Foo 实例生成时 就会调用 type 或其子类 mymeta.__call__, 里头调用了 Foo 的 __new__, __init__
    foo = Foo("foo")


    class MyMetaclass(type):
        def __new__(mcs, name, bases, dict, **kwargs):
            return type.__new__(mcs, name, bases, dict)
        def __init__(self, name, bases, dic):
            print('MyMetaclass init')
            super().__init__(name, bases, dic)

        def __call__(cls, *args, **kwargs):
            print("MyMetaclass.__call__():", args, kwargs)
            return type.__call__(cls, *args, **kwargs)
    # 说明了不是调用 MyMetaclass 的 __call__
    print(MyMetaclass("MyClass", (), {}))
