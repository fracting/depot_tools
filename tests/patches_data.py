      '@@ -3,6 +3,7 @@ bb\n'
      ' ccc\n'
      ' dd\n'
      ' e\n'
      '+FOO!\n'
      ' ff\n'
      ' ggg\n'
      ' hh\n')
  # To make sure the subdirectory was created as needed.
  NEW_SUBDIR = (
      'diff --git a/new_dir/subdir/new_file b/new_dir/subdir/new_file\n'
      'new file mode 100644\n'
      '--- /dev/null\n'
      '+++ b/new_dir/subdir/new_file\n'
      '@@ -0,0 +1,2 @@\n'
      '+A new file\n'
      '+should exist.\n')
