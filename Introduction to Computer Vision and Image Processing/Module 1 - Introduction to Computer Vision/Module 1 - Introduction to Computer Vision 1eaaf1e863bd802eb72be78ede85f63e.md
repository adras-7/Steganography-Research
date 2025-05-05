# Module 1 - Introduction to Computer Vision

**Learning Objectives:**

- Understand what computer vision is
- Apply Computer Vision Algorithms with Python and OpenCV
- Create custom classifiers
- Build a web app to classify images

# Introduction

Computer Vision seeks to provide computers with the ability to see and understand images

# Applications of Computer Vision

### **Video Search and Tagging**

- Problem: Searching for specific scenes in personal or movie videos is time-consuming.
- Solution: Use object recognition to automatically tag video scenes with keywords based on visible objects.
- Example: IBM demoed tagging video content to make videos searchable by object-based queries.
- Use Case: Security companies can search for a “blue van” across hours of surveillance footage instantly using object recognition.

### Infrastructure Inspection

- Challenge: Manually inspecting towers for rust or defects is dangerous and costly.
- Alternative: Take high-resolution photos from the ground (or drone safely away from wires).
- Approach:
    1. Split images into smaller grids.
    2. Apply a custom image classifier to:
        - Detect metal structures vs. non-metal.
        - Detect and grade rust severity (e.g., Grade 1 = minimal, Grade 6 = severe).
    3. Map results visually using a heatmap overlay to identify rusted areas.
- Impact: Scalable to thousands/millions of images; saves time and cost for insurance and engineering firms.

### Insurance Damage Assessment

- Example: Classifying damage (e.g., hail, ice pellet marks) on vehicles or property.
- Vision classifiers can:
    - Detect damage automatically.
    - Grade severity of damage with higher consistency than manual inspection.
- Benefit: Speeds up claim processing and reduces human error, potentially saving millions in costs.

# Practice Assessment Completion

![image.png](image.png)