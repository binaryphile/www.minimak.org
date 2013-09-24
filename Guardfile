# A sample Guardfile
# More info at https://github.com/guard/guard#readme

guard 'livereload', grace_period: 1 do
  watch('config.yml')
  watch(%r{partials/.+\.(md|html)$})
  watch(%r{media/.+\.(jpg|png|gif)})
  watch(%r{themes/artisteer/\w+/.+\.(css|js|html|jpg|png|gif)$})
  watch(%r{pages/.+\.(md|html)$})
end

