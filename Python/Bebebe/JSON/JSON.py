from typing import NoReturn

from ..example_classes import example_classes as ex

if __name__=="__main__":
    from Lab2.JSON import JSON as js
    from Lab2.example_classes import example_classes as ex
else:
    from ..JSON import JSON as js
    from ..example_classes import example_classes as ex

class ToJSON:
    @classmethod
    def to_json(cls, object_) -> str:
        content = cls.form_dict(object_)
        return cls.to_string(content)

    @classmethod
    def form_dict(cls, object_) -> dict:
        content = dict(item for item in object_.__class__.__dict__.items() if not item[0].startswith("__") and
                       not item[0].endswith("__"))
        content.update(item for item in object_.__dict__.items() if not item[0].startswith("__") and
                       not item[0].endswith("__"))
        return content


    @classmethod
    def to_string(cls, dict_) -> str:
        out_ = cls.dict_to_string(dict_)
        out_ = '{%s}' % out_[1:-1:1]
        return out_


    @classmethod
    def dict_to_string(cls, dict_) -> str:
        out_ = list('{')
        for key in dict_.keys():
            try:
                key.__getattribute__("__iter__")
                if isinstance(key, str):
                    out_.append('"%s":' % str(key))
                else:
                    out_.append('%s:' % cls.iterable_to_string(key))
            except AttributeError:
                out_.append('%s:' % str(key))
            try:
                dict_[key].__getattribute__("__iter__")
                if isinstance(dict_[key], str):
                    out_.append('"%s",' % str(dict_[key]))
                elif isinstance(dict_[key], dict):
                    out_.append('%s,' % cls.dict_to_string(dict_[key]))
                else:
                    out_.append('%s,' % cls.iterable_to_string(dict_[key]))
            except AttributeError:
                if isinstance(dict_[key], bool):
                    out_.append('%s,' % str(dict_[key]).lower())
                elif dict_[key] is None:
                    out_.append('null,')
                else:
                    out_.append('%s,' % str(dict_[key]))
        out_[-1] = out_[-1][0:-1]
        out_.append('}')
        return "".join(out_)

    #коллекцию в строку
    @classmethod
    def iterable_to_string(cls, iterable_) -> str:
        out_ = list('[')
        for item in iterable_:
            try:
                item.__getattribute__("__iter__")
                if isinstance(item, str):
                    out_.append('"%s",' % str(item))
                else:
                    out_.append('%s,' % cls.iterable_to_string(item))
            except AttributeError:
                if isinstance(item, bool):
                    out_.append('%s,' % str(item).lower())
                elif item is None:
                    out_.append('null,')
                else:
                    out_.append('%s,' % str(item))
        # удаление лишней запятой в конце
        out_[-1] = out_[-1][0:-1]
        out_.append(']')
        return "".join(out_)


def main() -> NoReturn:
    print(ToJSON.to_json(ex.FirstEx()))
    print(ToJSON.to_json(ex.SecondEx()))
    print(ToJSON.to_json(ex.ThirdEx()))


if __name__ == "__main__":
    main()
