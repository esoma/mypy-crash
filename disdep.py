
import os
import subprocess
import site

site_packages = [sp for sp in site.getsitepackages() if sp.endswith('site-packages')][0]
mypyc_dir =  site_packages + '\\mypyc'
mypyc_init = os.path.join(mypyc_dir, [
    f for f in os.listdir(mypyc_dir)
    if f.startswith('__init__')
    if f.endswith('.pyd')
][0])
mypyc_build = os.path.join(mypyc_dir, [
    f for f in os.listdir(mypyc_dir)
    if f.startswith('build')
    if f.endswith('.pyd')
][0])
mypyc_codegen_emitmodule = os.path.join(mypyc_dir + '\\codegen\\', [
    f for f in os.listdir(mypyc_dir + '\\codegen\\')
    if f.startswith('emitmodule')
    if f.endswith('.pyd')
][0])
mypyc_irbuild_main = os.path.join(mypyc_dir + '\\irbuild\\', [
    f for f in os.listdir(mypyc_dir + '\\irbuild\\')
    if f.startswith('main')
    if f.endswith('.pyd')
][0])
mypyc_irbuild_builder = os.path.join(mypyc_dir + '\\irbuild\\', [
    f for f in os.listdir(mypyc_dir + '\\irbuild\\')
    if f.startswith('builder')
    if f.endswith('.pyd')
][0])
mypyc_irbuild_ll_builder = os.path.join(mypyc_dir + '\\irbuild\\', [
    f for f in os.listdir(mypyc_dir + '\\irbuild\\')
    if f.startswith('ll_builder')
    if f.endswith('.pyd')
][0])


"""
print("__INIT__")
subprocess.run(['dependencies/dependencies.exe', '-imports', mypyc_init])
"""

print("BUILD")
subprocess.run(['dependencies/dependencies.exe', '-chain', mypyc_build])

"""
print("EMITMODULE")
subprocess.run(['dependencies/dependencies.exe', '-imports', mypyc_codegen_emitmodule])

print("MAIN")
subprocess.run(['dependencies/dependencies.exe', '-imports', mypyc_irbuild_main])

print("BUILDER")
subprocess.run(['dependencies/dependencies.exe', '-imports', mypyc_irbuild_builder])

print("LLBUILDER")
subprocess.run(['dependencies/dependencies.exe', '-imports', mypyc_irbuild_ll_builder])
"""