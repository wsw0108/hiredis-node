{
  'targets': [
    {
      'target_name': '<(module_name)',
      'sources': [
          'src/hiredis.cc'
        , 'src/reader.cc'
      ],
      'include_dirs': ["<!(node -e \"require('nan')\")"],
      'dependencies': [
        'deps/hiredis.gyp:hiredis-c'
      ],
      'defines': [
          '_GNU_SOURCE'
      ],
      'cflags': [
          '-Wall',
          '-O3'
      ]
    },
    {
      'target_name': 'action_after_build',
      'type': 'none',
      'dependencies': [ '<(module_name)' ],
      'copies': [
        {
          'files': [ '<(PRODUCT_DIR)/<(module_name).node' ],
          'destination': '<(module_path)'
        }
      ]
    }
  ]
}
