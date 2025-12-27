# miso_ramen_sequence.py
"""
Generate a UML sequence diagram (PlantUML) for the miso ramen workflow.

- Actors are kitchen stations: Refrigerator, PrepBoard, Skillet, Pot, Hob, Bowl, Strainer, Table.
- Each interaction line is annotated with:
    <T: t0, t, M:m u, A:a, E:e>

  Where:
    T: t0  = start time (relative, whole process starts at 00:00:00)
       t   = duration of this step (placeholder for now)
    M: m u = qualitative/quantitative measure (e.g. '1 batch', '2 min', '500 g')
    A: a   = optional adverb/adjective (e.g. 'gently', 'finely diced')
    E: e   = optional extra equipment notes (e.g. 'induction hob', 'cast iron skillet')
"""

from pathlib import Path


def build_plantuml() -> str:
    # For now, use simple placeholder values for timing & measures.
    # You can later customise each line with more realistic values.
    meta_default = "<T: 00:00:00, 00:00:30, M:1 step, A: , E: >"
    meta_simmer_long = "<T: 00:10:00, 01:00:00, M:long simmer, A:slowly, E:lid on>"
    meta_marinate_long = "<T: 01:30:00, 06:00:00, M:overnight soak, A: , E:fridge>"

    lines = [
        "@startuml",
        "title Miso Ramen Dinner - Station Sequence Diagram",
        "",
        "participant Refrigerator",
        "participant PrepBoard",
        "participant Skillet",
        "participant Pot",
        "participant Hob",
        "participant Bowl",
        "participant Strainer",
        "participant Table",
        "",
        "== Morning prep: Chashu (pork belly) ==",
        f"Refrigerator -> PrepBoard: Move pork belly and aromatics out {meta_default}",
        f"PrepBoard -> PrepBoard: Trim pork belly (if needed) {meta_default}",
        f"PrepBoard -> Skillet: Transfer pork belly to skillet {meta_default}",
        f"Skillet -> Hob: Sear pork belly on all sides {meta_default}",
        f"Hob --> Skillet: Pork belly browned {meta_default}",
        f"PrepBoard -> Pot: Transfer aromatics (garlic, ginger, spring onion) {meta_default}",
        f"Skillet -> Pot: Move seared pork belly to pot {meta_default}",
        f"Pot -> Pot: Add soy, sake, water, sugar, sesame, miso (braising liquid) {meta_default}",
        f"Pot -> Hob: Simmer on low heat (1–1.5 hours) {meta_simmer_long}",
        f"Hob --> Pot: Braised chashu in sauce {meta_default}",
        f"Pot -> Refrigerator: Cool and store chashu in braising liquid {meta_default}",
        "",
        "== Morning prep: Ramen eggs (ajitsuke tamago) ==",
        f"Refrigerator -> Pot: Move eggs and water for boiling {meta_default}",
        f"Pot -> Hob: Boil eggs 6–7 minutes {meta_default}",
        f"Hob --> Pot: Boiled eggs {meta_default}",
        f"Pot -> Bowl: Transfer eggs into cold water {meta_default}",
        f"Bowl -> PrepBoard: Cooled eggs ready to peel {meta_default}",
        f"PrepBoard -> PrepBoard: Crack shells and peel eggs {meta_default}",
        f"PrepBoard -> Bowl: Place peeled eggs in marinade {meta_default}",
        f"Pot -> Bowl: Add marinade (soy, water, sake/sugar or chashu liquid) {meta_default}",
        f"Bowl -> Refrigerator: Store marinating eggs (6–12 hours) {meta_marinate_long}",
        "",
        "== Evening: Toppings prep ==",
        f"Refrigerator -> PrepBoard: Retrieve chashu, eggs, vegetables, narutomaki, menma {meta_default}",
        f"PrepBoard -> PrepBoard: Slice chashu, spring onions, narutomaki {meta_default}",
        f"PrepBoard -> Bowl: Portion toppings into small bowls {meta_default}",
        f"Bowl -> Refrigerator: Hold toppings chilled until assembly {meta_default}",
        "",
        "== Evening: Miso ramen broth ==",
        f"Refrigerator -> PrepBoard: Move garlic, ginger, shallot {meta_default}",
        f"PrepBoard -> PrepBoard: Mince garlic, ginger, shallot {meta_default}",
        f"PrepBoard -> Pot: Transfer aromatics and ground pork (or mushrooms) {meta_default}",
        f"Pot -> Hob: Saute aromatics and pork in sesame oil {meta_default}",
        f"Hob --> Pot: Fragrant pork and aromatics {meta_default}",
        f"Pot -> Pot: Add doubanjiang, miso, sesame seeds, sugar, sake {meta_default}",
        f"Pot -> Pot: Add chicken stock / broth {meta_default}",
        f"Pot -> Hob: Simmer miso broth, adjust salt and white pepper {meta_default}",
        "",
        "== Evening: Noodles ==",
        f"Pot -> Hob: Boil water for noodles (separate pot) {meta_default}",
        f"Hob --> Pot: Rolling boil {meta_default}",
        f"Refrigerator -> PrepBoard: Move ramen noodles out (fresh or dry) {meta_default}",
        f"PrepBoard -> Pot: Add noodles to boiling water {meta_default}",
        f"Pot -> Hob: Cook noodles until al dente {meta_default}",
        f"Hob --> Pot: Noodles cooked {meta_default}",
        f"Pot -> Strainer: Drain noodles and shake off excess water {meta_default}",
        "",
        "== Assembly at serving time ==",
        f"Bowl -> Bowl: Warm serving bowls with hot water, then discard {meta_default}",
        f"Strainer -> Bowl: Place noodles into serving bowls {meta_default}",
        f"Pot -> Bowl: Ladle hot miso broth over noodles {meta_default}",
        f"Refrigerator -> Bowl: Add chashu slices and ramen eggs {meta_default}",
        f"Bowl -> Bowl: Add toppings (corn, menma, narutomaki, negi, nori) {meta_default}",
        f"Bowl -> Table: Serve miso ramen to diners {meta_default}",
        "",
        "@enduml",
    ]
    return "\n".join(lines)


def main():
    plantuml_text = build_plantuml()
    script_dir = Path(__file__).resolve().parent
    output_path = script_dir / "miso_ramen_sequence.puml"
    with output_path.open("w", encoding="utf-8") as f:
        f.write(plantuml_text)
    print(f"PlantUML sequence diagram written to {output_path}")


if __name__ == "__main__":
    main()
