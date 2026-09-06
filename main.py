"""
CitizenFix – Console CLI Application (Pure Conditional Statements Edition)
========================================================================
Built using only simple if/elif/else conditional statements and loops (No functions).
"""

import sys
from datetime import datetime

# Fix Windows console UTF-8 output encoding
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# INITIAL DEMO COMPLAINTS DATA (In-Memory Python List)
NOW_STR = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

complaints = [
    {
        "id": 101,
        "category": "Pothole",
        "description": "Large dangerous pothole on Main Street near 5th Ave.",
        "location": "Main Street & 5th Ave",
        "priority": "High",
        "status": "Pending",
        "resolution_notes": "",
        "created_at": NOW_STR
    },
    {
        "id": 102,
        "category": "Broken Streetlight",
        "description": "Flickering streetlight near park entrance.",
        "location": "Oak Street, Block B",
        "priority": "Medium",
        "status": "In Progress",
        "resolution_notes": "Technician assigned.",
        "created_at": NOW_STR
    },
    {
        "id": 103,
        "category": "Water Leak",
        "description": "Sidewalk water pipe leakage creating flooding.",
        "location": "Library Road",
        "priority": "High",
        "status": "Resolved",
        "resolution_notes": "Repaired pipe leak and restored pavement.",
        "created_at": NOW_STR
    },
    {
        "id": 104,
        "category": "Garbage",
        "description": "Overflowing waste bins near market center.",
        "location": "Market Road",
        "priority": "Low",
        "status": "Pending",
        "resolution_notes": "",
        "created_at": NOW_STR
    }
]

# MAIN CONTROL LOOP
while True:
    print("\n" + "=" * 65)
    print(" 🏙️  CitizenFix – Civic Issue Intelligence System (Console CLI)")
    print("=" * 65)
    print("1. 👤 Citizen Portal (Report Issue / View Complaints)")
    print("2. 🛡️ Municipal Officer Gateway (Login / Manage Tickets)")
    print("3. 📊 View Analytics Summary")
    print("4. 🚪 Exit")
    
    choice = input("\nSelect an option (1-4): ").strip()

    # =========================================================================
    # OPTION 1: CITIZEN PORTAL
    # =========================================================================
    if choice == '1':
        while True:
            print("\n--- 👤 CITIZEN PORTAL MENU ---")
            print("1. 📝 Report a New Civic Issue")
            print("2. 📋 View Live Reported Complaints")
            print("3. ⬅️ Back to Main Menu")
            cit_choice = input("\nSelect an option (1-3): ").strip()

            # --- SUB-OPTION 1.1: REPORT NEW ISSUE ---
            if cit_choice == '1':
                print("\n--- 📝 REPORT A NEW CIVIC ISSUE ---")
                print("Categories:")
                print("1. Pothole / Road Damage")
                print("2. Garbage / Waste Overflow")
                print("3. Water Leakage / Pipe Burst")
                print("4. Broken Streetlight")
                print("5. Other Issue")
                cat_choice = input("Select category (1-5): ").strip()

                if cat_choice == '1':
                    category = "Pothole"
                elif cat_choice == '2':
                    category = "Garbage"
                elif cat_choice == '3':
                    category = "Water Leak"
                elif cat_choice == '4':
                    category = "Broken Streetlight"
                else:
                    category = "Other"

                location = input("Enter Location / Address: ").strip()
                description = input("Enter Issue Description: ").strip()

                if location == "" or description == "":
                    print("❌ Location and description cannot be empty!")
                else:
                    # Calculate priority using conditionals
                    desc_lower = description.lower()
                    if ("danger" in desc_lower or "urgent" in desc_lower or "flooding" in desc_lower or "fire" in desc_lower or category == "Water Leak" or category == "Pothole"):
                        priority = "High"
                    else:
                        priority = "Medium"

                    # Generate new ID
                    if len(complaints) > 0:
                        new_id = max(c['id'] for c in complaints) + 1
                    else:
                        new_id = 101

                    new_ticket = {
                        "id": new_id,
                        "category": category,
                        "description": description,
                        "location": location,
                        "priority": priority,
                        "status": "Pending",
                        "resolution_notes": "",
                        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    complaints.insert(0, new_ticket)
                    print(f"\n✅ SUCCESS! Complaint Ticket #{new_id} created successfully.")

            # --- SUB-OPTION 1.2: VIEW COMPLAINTS ---
            elif cit_choice == '2':
                print(f"\n--- 📋 LIVE COMPLAINTS FEED ({len(complaints)} total) ---")
                if len(complaints) == 0:
                    print("No complaints reported yet.")
                else:
                    for c in complaints:
                        if c['status'] == "Pending":
                            status_icon = "⏳"
                        elif c['status'] == "In Progress":
                            status_icon = "🔄"
                        else:
                            status_icon = "✅"

                        print(f"\n -------------------------------------------------------------")
                        print(f" Ticket #{c['id']} [{c['category'].upper()}] - Priority: {c['priority']}")
                        print(f" Status: {status_icon} {c['status']}")
                        print(f" Location: {c['location']}")
                        print(f" Reported: {c['created_at']}")
                        print(f" Details:  {c['description']}")
                        if c['resolution_notes'] != "":
                            print(f" 📝 Officer Note: {c['resolution_notes']}")
                        print(f" -------------------------------------------------------------")

            # --- SUB-OPTION 1.3: BACK TO MAIN MENU ---
            elif cit_choice == '3':
                break
            else:
                print("❌ Invalid option. Try again.")

    # =========================================================================
    # OPTION 2: MUNICIPAL OFFICER GATEWAY
    # =========================================================================
    elif choice == '2':
        print("\n--- 🛡️ MUNICIPAL OFFICER LOGIN ---")
        print("Tip: Use default credentials (officer@city.gov / Officer@123)")
        email = input("Enter Officer Email: ").strip()
        password = input("Enter Password: ").strip()

        # LOGIN AUTHENTICATION CONDITIONAL
        if email.lower() == "officer@city.gov" and password == "Officer@123":
            print(f"\n✅ Welcome Municipal Officer ({email})!")

            while True:
                print("\n--- 🛡️ OFFICER COMMAND CENTER MENU ---")
                print("1. 🛠️ View & Manage Complaint Queue")
                print("2. ✏️ Update Ticket Status & Resolution Notes")
                print("3. 📊 View Metrics Summary")
                print("4. 🚪 Logout")
                off_choice = input("\nSelect an option (1-4): ").strip()

                # --- OFFICER SUB-OPTION 2.1: VIEW QUEUE ---
                if off_choice == '1':
                    print("\nFilter Status:")
                    print("1. All Issues")
                    print("2. Pending")
                    print("3. In Progress")
                    print("4. Resolved")
                    flt_choice = input("Select filter (1-4): ").strip()

                    if flt_choice == '2':
                        target_status = "Pending"
                    elif flt_choice == '3':
                        target_status = "In Progress"
                    elif flt_choice == '4':
                        target_status = "Resolved"
                    else:
                        target_status = "All"

                    print(f"\n--- 🛠️ COMPLAINT QUEUE [{target_status.upper()}] ---")
                    count = 0
                    for c in complaints:
                        if target_status == "All" or c['status'] == target_status:
                            count += 1
                            if c['status'] == "Pending":
                                status_icon = "⏳"
                            elif c['status'] == "In Progress":
                                status_icon = "🔄"
                            else:
                                status_icon = "✅"

                            print(f"\n -------------------------------------------------------------")
                            print(f" Ticket #{c['id']} [{c['category'].upper()}] - Priority: {c['priority']}")
                            print(f" Status: {status_icon} {c['status']}")
                            print(f" Location: {c['location']}")
                            print(f" Reported: {c['created_at']}")
                            print(f" Details:  {c['description']}")
                            if c['resolution_notes'] != "":
                                print(f" 📝 Officer Note: {c['resolution_notes']}")
                            print(f" -------------------------------------------------------------")

                    if count == 0:
                        print("No complaints found for this status.")

                # --- OFFICER SUB-OPTION 2.2: UPDATE TICKET STATUS ---
                elif off_choice == '2':
                    ticket_input = input("\nEnter Ticket ID to update (e.g. 101): ").strip()
                    if ticket_input.isdigit():
                        target_id = int(ticket_input)
                        found_ticket = None
                        for c in complaints:
                            if c['id'] == target_id:
                                found_ticket = c
                                break

                        if found_ticket is None:
                            print(f"❌ Ticket #{target_id} not found.")
                        else:
                            print(f"\nEditing Ticket #{target_id} [{found_ticket['category']}]")
                            print("Select New Status:")
                            print("1. Pending")
                            print("2. In Progress")
                            print("3. Resolved")
                            st_choice = input("Select status (1-3): ").strip()

                            if st_choice == '1':
                                new_st = "Pending"
                            elif st_choice == '2':
                                new_st = "In Progress"
                            elif st_choice == '3':
                                new_st = "Resolved"
                            else:
                                new_st = None

                            if new_st is None:
                                print("❌ Invalid status choice.")
                            else:
                                notes = input("Enter Resolution Notes / Officer Remarks: ").strip()
                                found_ticket['status'] = new_st
                                found_ticket['resolution_notes'] = notes
                                print(f"\n✅ SUCCESS! Ticket #{target_id} updated to '{new_st}'.")
                    else:
                        print("❌ Please enter a valid numerical Ticket ID.")

                # --- OFFICER SUB-OPTION 2.3: METRICS ---
                elif off_choice == '3':
                    total_cnt = len(complaints)
                    pending_cnt = sum(1 for c in complaints if c['status'] == 'Pending')
                    progress_cnt = sum(1 for c in complaints if c['status'] == 'In Progress')
                    resolved_cnt = sum(1 for c in complaints if c['status'] == 'Resolved')

                    print("\n--- 📊 MUNICIPAL METRICS SUMMARY ---")
                    print(f" Total Logged Complaints:  {total_cnt}")
                    print(f" ⏳ Pending Tickets:        {pending_cnt}")
                    print(f" 🔄 In Progress Tickets:    {progress_cnt}")
                    print(f" ✅ Resolved Tickets:       {resolved_cnt}")

                # --- OFFICER SUB-OPTION 2.4: LOGOUT ---
                elif off_choice == '4':
                    print("\n🚪 Logged out of Municipal Officer Panel.")
                    break
                else:
                    print("❌ Invalid option. Try again.")

        else:
            print("\n❌ Login Failed: Invalid email or password.")

    # =========================================================================
    # OPTION 3: PUBLIC ANALYTICS SUMMARY
    # =========================================================================
    elif choice == '3':
        total_cnt = len(complaints)
        pending_cnt = sum(1 for c in complaints if c['status'] == 'Pending')
        progress_cnt = sum(1 for c in complaints if c['status'] == 'In Progress')
        resolved_cnt = sum(1 for c in complaints if c['status'] == 'Resolved')

        print("\n--- 📊 PUBLIC CIVIC ANALYTICS SUMMARY ---")
        print(f" Total Logged Complaints:  {total_cnt}")
        print(f" ⏳ Pending Tickets:        {pending_cnt}")
        print(f" 🔄 In Progress Tickets:    {progress_cnt}")
        print(f" ✅ Resolved Tickets:       {resolved_cnt}")
        input("\nPress Enter to return to main menu...")

    # =========================================================================
    # OPTION 4: EXIT PROGRAM
    # =========================================================================
    elif choice == '4':
        print("\n👋 Thank you for using our CitizenFix platform. Goodbye!")
        sys.exit(0)

    else:
        print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")
