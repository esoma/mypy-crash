
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

subprocess.run(['dependencies/dependencies.exe', '-imports', mypyc_init])
