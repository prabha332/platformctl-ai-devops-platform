def ai_debug(issue):

    knowledge_base = {
        "CrashLoopBackOff":
        "Container failing repeatedly. Check logs or increase memory limits.",

        "ImagePullBackOff":
        "Container image not found. Verify image name or registry access.",

        "OOMKilled":
        "Pod killed due to memory exhaustion. Increase resources."
    }

    for key in knowledge_base:
        if key.lower() in issue.lower():
            print("\nAI Diagnosis:")
            print(knowledge_base[key])
            return

    print("AI could not identify issue.")
