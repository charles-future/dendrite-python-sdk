    else:
        print(result.stdout)


# Step 1: Clean the dist directory
print("Cleaning the dist directory...")
run_command("rm -rf dist/*")

# Step 2: Build the package
print("Building the package...")
run_command("poetry build")

# Step 3: Publish the package to PyPI
print("Publishing the package to PyPI...")
run_command("poetry publish")

print("Done!")
# auto-comment Sat 11/29/2025  2:32:51 (docs/styles-5429) 
