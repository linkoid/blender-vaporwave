bl_info = {
    "name": "Vaporwave",
    "author": "@linkoid",
    "version": ("alpha", 2021, 6, 18),
    "blender": (2, 80, 0),
    "location" : "View 3D > Sidebar > Vaporwave",
    "description" : "The vaporwave add-on aids in the creation of vaporwave meshes.",
    "warning": "",
    "wiki_url": "https://github.com/linkoid/blender-vaporwave/blob/main/README.md",
    "tracker_url": "https://github.com/linkoid/blender-vaporwave",
    "category": "Modeling"
}

import_modules = ["space_view3d_vaporwave"]
imported_modules = dict()

if "bpy" in locals():
    import imp

    for module in imported_modules.values():
        imp.reload(module)

else:
    import importlib
    for module_name in import_modules:
        module = imp.import_modules(f".{module_name}")
        locals()[module_name] = module
        imported_modules[module_name] = module


class AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

classes = {
    AddonPreferences,
}


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    for mod in imported_modules.values():
        try:
            mod.register()
        except:
            pass


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
    for mod in imported_modules.values():
        try:
            mod.unregister()
        except:
            pass


if __name__ == "__main__":
    register()
