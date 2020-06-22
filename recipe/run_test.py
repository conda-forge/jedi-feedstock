import time
import jedi

print("default jedi environment", jedi.api.environment.get_default_environment())
print("jedi cache", jedi.settings.cache_directory)

SOURCE_TEMPLATE = """
import {module}
{module}."""

def complete_one(module):
    print(module, end="\t")
    start = time.time()
    script = jedi.Script(SOURCE_TEMPLATE.format(module=module))
    completions = len(script.complete(3, len("{}.".format(module))))
    end = time.time()
    print("\t", completions, end - start)
    assert completions

print(complete_one("jedi"))
