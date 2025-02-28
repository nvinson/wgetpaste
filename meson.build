project(
  'wgetpaste',
  license: 'MIT',
  license_files: 'LICENSE',
  version: '2.35.0',
  meson_version: '>=1.1.0',
)

config_data = configuration_data()
config_data.set('WGETPASTE_SHEBANG', get_option('shebang'))
config_data.set('WGETPASTE_VERSION', meson.project_version())
configure_file(
  output: 'wgetpaste',
  input: 'wgetpaste',
  configuration: config_data,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'rwxr-xr-x'
)

install_data(
  '_wgetpaste',
  install_dir: get_option('datadir') / get_option('zsh-completions-dir'),
  install_mode: 'rw-r--r--'
)
