1. University Selection Criteria and Structure
   Requested a detailed list of universities in Berlin and surrounding areas, grouped by type (e.g., Universität, Technische Universität, Fachhochschule, etc.).
   Asked for additional fields for each faculty/department, including:
   Description of each faculty.
   Address where the study takes place.
   Contact Information, including webpage, email, and phone for admissions.
   City as a mandatory field referencing an enumerated list.
   Subject, referencing an enumerated list of fields of study (e.g., Architecture, Mathematics, etc.).
   Requested restructuring of the YAML file to move faculties one level up, making them nodes directly under their universities.
2. Specific Focus on Barbora's Preferences
   Highlighted that Barbora prefers dual vocational training systems (Duale Ausbildung), where she can combine practical experience with academic studies.
   Emphasized future-proof fields that align with societal and technological changes, ensuring her skills remain in demand and not easily replaceable by AI.
   Stressed the importance of hands-on experience and creativity, prioritizing architecture, design, engineering, and mathematics as her primary focus areas.
   Requested information on universities with strong programs in these areas.
3. Enhancements to Faculty Information
   Made the Subject field mandatory for each faculty, ensuring it refers to an enumerated list of study areas.
   Made the Description field mandatory, requiring meaningful and specific content for every faculty.
   Requested the addition of a Program sub-block under faculties, describing study specializations and providing a URL for more details where possible.
   Asked for all faculties to include City as a field, referencing a predefined list of cities.
4. Structuring Data for Long-Term Use
   Requested grouping of universities by city rather than just Berlin and outside Berlin, considering the future possibility of including other cities, even outside Germany.
   Sought flexibility in the data structure to accommodate interdisciplinary programs, specialized study groups, and multiple locations for the same university.
5. Detailed Summary for Decision-Making
   Requested a full display of updated and restructured YAML files with all fields and adjustments.
   Highlighted the need for meaningful descriptions in faculty fields, avoiding placeholders like "Unknown" or "Not Provided."


### **1\. University Selection Criteria and Structure**

- **Group Universities by Type**:
   - Classify universities into categories such as:
      - **Universität (Traditional Research Universities)**
      - **Technische Universität (Technical Universities)**
      - **Fachhochschule (Universities of Applied Sciences)**
      - **Art or Music Academies**

- **Faculty Details for Each University**:
   - Add detailed fields for each faculty, including:
      - **Description**: A clear and specific summary of what the faculty offers.
      - **Address**: Location where the courses are conducted.
      - **Contact Information**: Include:
         - Webpage URL
         - Email address for admissions
         - Phone number for inquiries
      - **City**: A mandatory field referencing an enumerated list of cities.
      - **Subject**: Must align with an enumerated list of study fields (e.g., Architecture, Mathematics, etc.).

* * *

### **2\. Specific Focus on Barbora's Preferences**

- **Dual Vocational Training (Duale Ausbildung)**:
   - Highlight universities and programs offering dual study options that blend **practical training** with **academic education**.
- **Future-Proof Fields**:
   - Focus on fields that align with societal and technological changes, such as:
      - Architecture
      - Design
      - Engineering
      - Mathematics
   - Emphasize programs fostering **creativity**, **practical experience**, and skills less susceptible to automation or AI disruption.
- **Recommended Institutions**:
   - Identify universities with strong, hands-on programs in the above fields.

* * *

### **3\. Enhancements to Faculty Information**

- **Mandatory Fields**:
   - **Subject**: Each faculty must reference an enumerated list of subjects.
   - **Description**: Require meaningful, detailed descriptions. Generic placeholders like "Not Provided" are not acceptable.
- **Program Sub-Block**:
   - Include a sub-block for each faculty's study programs, specifying:
      - **Specializations**
      - A URL for more details

- **City Field**:
   - Make the city a required field for each faculty to enable better filtering and searching.

* * *

### **4\. Structuring Data for Long-Term Use**

- **Group Universities by City**:
   - Organize universities first by city rather than just "Berlin" or "outside Berlin," allowing for the inclusion of universities from other regions or countries in the future.
- **Flexibility in Structure**:
   - Prepare the YAML structure to accommodate:
      - **Interdisciplinary Programs**: Faculties or programs crossing multiple study fields.
      - **Specialized Study Groups**: Niche areas of study within a larger faculty.
      - **Multiple Locations**: Universities with campuses in different cities or regions.

* * *

### **5\. Detailed Summary for Decision-Making**

- **YAML File Display**:
   - Present a full YAML structure with all requested adjustments and updates.
   - Ensure meaningful content for every field, with specific focus on the **Description** and **Program** fields.
   - Provide an organized, standardized format for future scalability and decision-making.