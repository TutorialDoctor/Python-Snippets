*The __init__.py files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name, such as string, from unintentionally hiding valid modules that occur later (deeper) on the module search path. In the simplest case, __init__.py can just be an empty file, but it can also execute initialization code for the package or set the __all__ variable, described later.*

*In addition to labeling a directory as a Python package and defining __all__, __init__.py allows you to define any variable at the package level. Doing so is often convenient if a package defines something that will be imported frequently, in an API-like fashion. This pattern promotes adherence to the Pythonic "flat is better than nested" philosophy.*

*The __init__.py file makes Python treat directories containing it as modules. Furthermore, this is the first file to be loaded in a module, so you can use it to execute code that you want to run each time a module is loaded, or specify the submodules to be exported.*

A folder that has an __init__.py file in it is treated as a module.The init file is the first file to be loaded in a module and can be used to execute code you want to run each time a module is loaded. You can also specify the submodules to be exported.

Works like the __init__ method of a class
