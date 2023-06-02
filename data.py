import random

people = [
    {
        "name": name,
        "image": f"https://picsum.photos/id/{random.randint(1,50)}/40",
    }
    for name in ["russell", "juan", "enrico"]
]

spaces = ["My Space", "Face Book", "Yaw Who"]


sentences = [
    "The blue cat jumped over the lazy dog.",
    "The old man sat on the bench and read a book.",
    "The young woman ran through the field of flowers.",
    "The bird flew away into the sky.",
    "The car drove down the street.",
    "The house was built on a hill.",
    "The tree stood tall in the forest.",
    "The river flowed through the valley.",
    "The sun shone brightly in the sky.",
    "The moon and stars twinkled in the night sky.",
    "The blue cat jumped over the lazy dog.",
    "The old man sat on the bench and read a book.",
    "The young woman ran through the field of flowers.",
    "The bird flew away into the sky.",
    "The car drove down the street.",
    "The house was built on a hill.",
    "The tree stood tall in the forest.",
    "The river flowed through the valley.",
    "The sun shone brightly in the sky.",
    "The moon and stars twinkled in the night sky.",
]

replies = [
    "I see your point, but I don't think it's that big of a deal.",
    "I agree with you to an extent, but I think you're overreacting.",
    "I don't see why this is such a big deal.",
    "I think you're making a mountain out of a molehill.",
    "I don't think it's worth getting worked up about.",
    "I think you're taking this too seriously.",
    "I think you're reading too much into it.",
    "I think you're blowing this out of proportion.",
    "I think you're overreacting.",
    "I think you're being ridiculous.",
    "I actually agree with you.",
    "I think you're right.",
    "I think you make a good point.",
    "I see where you're coming from.",
    "I think I agree with you.",
    "I think you're on to something.",
    "I think you're right on the money.",
    "I think you're spot on.",
    "I think you're dead on.",
    "I think you're absolutely right.",
    "I strongly disagree with you.",
    "I think you're wrong.",
    "I think you're mistaken.",
    "I think you're off base.",
    "I think you're full of it.",
]


task_names = [
    "Write a blog post",
    "Create a presentation",
    "Design a website",
    "Develop a new product",
    "Conduct market research",
    "Analyze data",
    "Write a report",
    "Give a presentation",
    "Meet with a client",
    "Close a deal",
    "Negotiate a contract",
    "Hire a new employee",
    "Fire an employee",
    "Train an employee",
    "Give feedback to an employee",
    "Review a project",
    "Make a decision",
    "Solve a problem",
    "Brainstorm new ideas",
    "Manage a team",
    "Lead a project",
    "Delegate tasks",
    "Motivate others",
    "Create a positive work environment",
    "Celebrate success",
]

task_descriptions = [
    "Write blog about topic",
    "Create presentation for meeting",
    "Design website for company",
    "Develop new product for market",
    "Research target audience",
    "Analyze data to find insights",
    "Write report on findings",
    "Present to stakeholders",
    "Meet with client to discuss project",
    "Close deal with client to secure sale",
    "Negotiate contract with client to agree terms",
    "Hire new employee to fill role",
    "Fire employee for performance issues",
    "Train employee on new skills",
    "Give feedback to employee on performance",
    "Review project to ensure quality",
    "Make decision on course of action",
    "Solve problem to overcome obstacle",
    "Brainstorm new ideas to generate innovation",
    "Manage team of employees",
    "Lead project to completion",
    "Delegate tasks to team members",
    "Motivate team members to achieve goals",
    "Create positive work environment for employees",
    "Celebrate success with team members",
]


quill_mods = [
    [{"header": "1"}, {"header": "2"}, {"font": []}],
    [{"size": []}],
    ["bold", "italic", "underline", "strike", "blockquote"],
    [{"list": "ordered"}, {"list": "bullet"}, {"indent": "-1"}, {"indent": "+1"}],
    ["link", "image"],
    ["clean"],
]
