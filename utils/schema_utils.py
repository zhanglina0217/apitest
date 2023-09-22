import json

from genson import SchemaBuilder
from jsonschema.validators import validate


class SchemaUitls:

    @classmethod
    def generate_jsonschema(cls, obj):
        # 实例化jsonschema
        builder = SchemaBuilder()
        # 传入被转换的对象
        builder.add_object(obj)
        # 转换成 schema 数据
        return builder.to_schema()

    @classmethod
    def generate_jsonschema_file(cls, file_path, obj):
        schema_obj = cls.generate_jsonschema(obj)
        # 打开一个文件，要求有写入权限
        with open(file_path, "w") as f:
            json.dump(schema_obj, f)

    @classmethod
    def schema_validate(cls, obj, schema):
        try:

            # 读取文件中的schema信息

            validate(instance=obj, schema=schema)
            return True
        except Exception as e:
            return False

    @classmethod
    def schema_validate_by_file(cls, obj, file_path):

        schema = json.load(open(file_path))

        return cls.schema_validate(obj, schema)


if __name__ == '__main__':
    data = {'id': 8335, 'period': '2037年下半年',
            'object': {'id': 9264, 'showName': '大千okr-okrrrrrrrrrrrrrrooooookkkkkkkkkkkkkkkkkkpppppppp',
                       'showNamePinyin': 'daqianokrokrrrrrrrrrrrrrrooooookkkkkkkkkkkkkkkkkkpppppppp', 'hasAvatar': True,
                       'avatar': 'https://rishiqing-avatar.oss-cn-beijing.aliyuncs.com/beta-test/9413/1657701143995_avatar.png'},
            'score': '-', 'level': '-', 'stage': 'scoring', 'rule': 999}
    # print(SchemaUitls.generate_jsonschema_file("schema_performance_my.json", data))
    print(SchemaUitls.schema_validate_by_file(data, "schema_performance_my.json"))
