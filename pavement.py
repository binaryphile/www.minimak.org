import subprocess as sub
from paver.easy import *
import yaml
from unipath import Path
from bunch import *

def bunchify_yaml_file(filename):
    '''
    Load and bunchify a yaml file

    '''
    yaml_data = yaml.safe_load(Path(filename).read_file())
    result = bunchify(yaml_data)
    return result


@task
@cmdopts([('opts=', 'o', 'an options file')])
def auto(options):
    '''
    Load my task options

    '''
    this_file = Path(__file__)
    cfg_file = this_file.absolute().parent.child('pavement_config.yml')
    cfg = bunchify_yaml_file(cfg_file)
    options.cfg = cfg


@task
def clean(options):
    '''
    Clean the last build

    '''
    cfg = options.cfg.default
    clean_dirs = [_dir % cfg for _dir in cfg.clean_dirs]
    clean_dirs = [Path(_dir).absolute() for _dir in clean_dirs if _dir and Path.isdir(_dir)]
    for _dir in clean_dirs:
        if _dir.components() < 4:
            print 'Directory %s is too close to the root.  Skipping.' % _dir
            continue
        cmd = 'rd /s /q %(_dir)s' % locals()
        sub.check_call(cmd, shell=True)


@task
def run(options):
    '''
    Run the development server.

    '''
    cmd = 'rackup.bat -p 3000'
    sub.check_call(cmd)


@task
def build(options):
    '''
    Build the distribution.

    '''
    cfg = options.cfg.default
    cmd = 'git commit -a > nul'
    print 'Committing...'
    sub.call(cmd, shell=True)
    cmd = 'git push > nul'
    print 'Pushing...'
    sub.check_call(cmd, shell=True)
    cmd = 'ruhoh.bat compile %(build_dir)s > nul' % cfg
    print 'Compiling...'
    sub.check_call(cmd, shell=True)
    cmd = r'xcopy /y /s %(contrib_dir)s %(build_dir)s > nul' % cfg
    print 'Copying contrib files...'
    sub.check_call(cmd, shell=True)
    print 'Done.'


@task
@needs(['build'])
def release(options):
    '''
    Build and release the site to S3
    
    '''
    print 'Releasing...'
    print 'Done'


if __name__ == '__main__':
    import paver.tasks
    paver.tasks.main()
