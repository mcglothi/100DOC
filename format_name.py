def format_name(f_name, l_name):
  """Take a first and last name and format it to return the title case version of the name."""
  formatted_fname = f_name.title()
  formatted_lname = l_name.title()
  return f"{formatted_fname} {formatted_lname}"


print(format_name("tIM", "mCgLOThin"))
