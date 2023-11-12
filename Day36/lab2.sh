#! /usr/bin/zsh
# =========================================1:-
# print "What is your name?"
# read name
# print "hello $name"
# =========================================2:-
# touch {s1,s2}.sh
# chmod u+x s*
# =========================================3:-
# source="$1"
# destination="$2"
# if [ -d "$destination" ]; then
#     cp -r "$source" "$destination"
# else
#     cp "$source" "$destination"
# fi

# if [ -d "${@: -1}" ]; then
#     cp $*
# else
#     cp $1 $2
# fi
# =========================================4:-
# if [ "$#" -eq "0" ]; then
#     cd ~
# else
#     cd "$1"
# fi
# source lab2.sh
# =========================================5:-
# if [ "$#" -eq 0 ]; then
#     ls .
# else
#     ls "$1"
# fi
# =========================================6:-


# if [ "$#" -gt 0 ]; then
#     case "$1" in
#         -l)
#             ls -l "$2"
#             shift
#         ;;
#         -a)
#             ls -a "$2"
#             shift
#         ;;
#         -d)
#             ls -d "$2"
#             shift
#         ;;
#         -i)
#             ls -i "$2"
#             shift
#         ;;
#         -R)
#             ls -R "$2"
#             shift
#         ;;
#         *)
#             echo "Unknown option: $1"
#             exit 1
#             ;;
#     esac
# else
#     ls .
# fi

# =========================================7:-
# target="$1"
# if [ -f "$target" ]; then
#     echo "$target is a regular file."
#     if [ -r "$target" ]; then
#         echo "Read permission: Yes"
#     else
#         echo "Read permission: No"
#     fi
#     if [ -w "$target" ]; then
#         echo "Write permission: Yes"
#     else
#         echo "Write permission: No"
#     fi
#     echo "Execute permission: No"

# elif [ -d "$target" ]; then
#     echo "$target is a directory."
#     if [ -r "$target" ]; then
#         echo "Read permission: Yes"
#     else
#         echo "Read permission: No"
#     fi
#     if [ -w "$target" ]; then
#         echo "Write permission: Yes"
#     else
#         echo "Write permission: No"
#     fi
#     if [ -x "$target" ]; then
#         echo "Execute permission: Yes"
#     else
#         echo "Execute permission: No"
#     fi

# else
#     echo "$target is neither a regular file nor a directory."
# fi
# =========================================8:-
# echo "plaese enter your logname:"

# read logname

# home_directory="/home/$logname"
# if [ ! -d "$home_directory" ]; then
#     echo "Home directory for $logname does not exist."
#     exit 1
# fi

# echo "Listing files and directories in $home_directory:"
# ls -l "$home_directory"

# tmp_directory="/tmp/$logname"
# echo "Copying files and directories to $tmp_directory..."
# mkdir -p "$tmp_directory"
# cp -r "$home_directory"/* "$tmp_directory"

# echo "Getting current process status for $logname:"
# ps -u "$logname"
# =========================================