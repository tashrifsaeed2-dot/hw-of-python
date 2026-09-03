member_name = input("Enter member's full name: ")
club_name = input("Enter club's name: ")
membership_number = int(input("Enter membership number: "))

join_year = 2025
is_active = True

membership_str = str(membership_number)
join_year_str = str(join_year)
active_str = str(is_active)

name_prefix = member_name[:3].upper()
club_prefix = club_name[:3].upper()

rev_number = membership_str[::-1]
padded_rev = (rev_number + "00")[:2]
number_suffix = padded_rev[::-1]

badge_code = name_prefix + "-" + number_suffix

badge = "===================================\n"
badge += "        SCHOOL CLUB BADGE        \n"
badge += "===================================\n"
badge += "Member Name    : " + member_name + "\n"
badge += "Club           : " + club_name + "\n"
badge += "Membership No. : " + membership_str + "\n"
badge += "Join Year      : " + join_year_str + "\n"
badge += "Active Member  : " + active_str + "\n"
badge += "Badge Code     : " + badge_code + "\n"
badge += "==================================="

print(badge)