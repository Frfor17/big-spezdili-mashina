# rn its not working


# щас это не пашет, но надо сделать чтобы пахало

# чтобы к примеру можно было добавить окопы в свой билд


# also cool feature to make is like, make it possible to easily to add to your build the ghost hud
# like i mean, one button and now your build have ghost hud

# or trenches
# like - one button and now your build have trenches


















import os
import shutil
import json
from dmi import parse_states

# def porter(dmi_path, config_json):
#     # 1. Копируем DMI куда надо
#     dmi_name = os.path.basename(dmi_path)
#     target_dir = "icons/obj/"  # или из config
#     target_path = f"{target_dir}/{dmi_name}"
#     os.makedirs(target_dir, exist_ok=True)
#     shutil.copy2(dmi_path, target_path)
#     print(f"DMI закинут в {target_path}")
    
#     # 2. Парсим states (без полного открытия — только метаданные)
#     states = parse_states(target_path)  # ['base', 'on', 'dir1', 'dir2', etc.]
    
#     # 3. Читаем config
#     config = json.loads(config_json)
#     obj_name = config['object']
#     parent = config.get('parent', '/obj/item')
#     icon = f"'icons/obj/{dmi_name}'"
    
#     # 4. Генерим код с ДОБАВЛЕНИЕМ всех states
#     dm_code = f"""{obj_name}
#     parent_type = {parent}
#     icon = {icon}
#     icon_state = "{states[0]}"  // дефолт первый state
# """
    
#     # Добавляем каждый state как var или proc
#     for state in states[1:]:  # первый уже в icon_state
#         dm_code += f"""
#     var/{state}_state = "{state}"""  # или icon_state = "{state}" в init()
    
#     # Дополнительные vars из config
#     for var_name, var_val in config.get('vars', {}).items():
#         dm_code += f"\n    {var_name} = {var_val}"
    
#     with open(f"{obj_name}.dm", 'w') as f:
#         f.write(dm_code)
    
#     print(f"Код сгенерирован: {obj_name}.dm со states: {states}")

# # Использование: python porter.py sprites.dmi config.json
