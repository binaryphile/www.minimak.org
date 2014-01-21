# A sample Guardfile
# More info at https://github.com/guard/guard#readme

guard 'livereload', grace_period: 1 do
  watch('data.yml')
  watch(%r{partials/.+\.(md|html)$})
  watch(%r{media/.+\.(jpg|png|gif)})
  watch(%r{foundation/\w+/.+\.(css|js|html)$})
  watch(%r{_root/.+\.(md|html)$})
end

# Guard::Compass
#
# You don't need to configure watchers for guard 'compass' declaration as they generated
# from your Compass configuration file. You might need to define the Compass working directory
# and point to the configuration file depending of your project structure.
#
# Available options:
#
# * :workging_directory => Define the Compass working directory, relative to the Guardfile directory
# * :configuration_file => Path to the Compass configuration file, relative to :project_path
#
# Like usual, the Compass configuration path are relative to the :project_path

# guard 'compass', :project_path => 'not_current_dir', :configuration_file => 'path/to/my/compass_config.rb'
guard :compass, project_path: 'foundation', configuration_file: 'foundation/config.rb'

