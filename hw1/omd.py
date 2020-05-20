from dataclasses import dataclass

SEPARATOR = '_' * 30


@dataclass
class StoryStep:
    story: str
    yes: int = 0
    no: int = 0
    is_end: bool = False


story = {
    0: StoryStep(
        story="Утка-маляр 🦆 решила выпить зайти в бар. "
              "Взять ей зонтик? ⛱",
        yes=1,
        no=2,
    ),
    1: StoryStep(
        story="Утка взяла зонтик и вышла из дома. "
              "Поехать ей на трамвае? 🚋",
        yes=3,
        no=4
    ),
    2: StoryStep(
        story="Утка решила не брать зонт и отправилась в бар, но как "
              "обычно бывает по закону подлости, начался очень сильный дождь. "
              "МЧС присылал СМС, но уток же нет телефона. Замерзшая, усталая "
              "утка вернулась домой. ",
        is_end=True
    ),
    3: StoryStep(
        story="В травмае ее арестовали, так как у утки не было денег. "
              "Аргументы о том, что у нее нет карманов и поэтому негде хранить "
              "деньги не помогли 👮",
        is_end=True
    ),
    4: StoryStep(
        story="Дойдя неспешным шагом до бара, утка с удивлением узнала, что бар почему-то закрыт."
              "Может лучше пойти домой? 🏠",
        yes=5,
        no=6
    ),
    5: StoryStep(
        story='Утка зашла в магазин, купила свое любимое пиво "Жатецкая утка" 🍺'
              'и отправилась домой 🏠. Как только она зашла домой, начался сильный '
              'ливень. Весь вечер она смотрела в окно и любовалась стихией',
        is_end=True

    ),
    6: StoryStep(
        story='Утка решила отправится в следующий бар, но и он оказался закрыт.'
              'Может все-таки ей пойти домой? 🏠',
        yes=5,
        no=7
    ),
    7: StoryStep(
        story='Дойдя до следующего бара, утка увидела что и он закрыт. Оказывается, '
              'все бары в городе были закрыты потому, что ввели карантин. '
              'Растроенная утка обреченно решила отправится домой. Ей поехать на трамвае?',
        yes=3,
        no=5
    )
}


def next_step(step_id: int):
    story_step = story.get(step_id)
    print(SEPARATOR)

    if not story_step:
        print("Что-то пошло не так! 🦆🦆🦆")
        exit()

    print(story_step.story)
    if story_step.is_end:
        print('Конец!')
        exit()

    option = ""
    options = {"да": True, "нет": False}
    while option not in options:
        print("Выберите: {}/{}".format(*options))
        option = input()

    if options[option]:
        next_step(story_step.yes)
    else:
        next_step(story_step.no)


if __name__ == "__main__":
    next_step(0)
