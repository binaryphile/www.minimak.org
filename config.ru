require 'rack'
require 'ruhoh'
require 'rack-livereload'
use Rack::LiveReload, no_swf: true
run Ruhoh::Program.preview

# To preview your blog in "production" mode:
# run Ruhoh::Program.preview(:env => 'production')
